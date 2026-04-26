"""
aiohttp 客户端（Client）基础示例：ClientSession、GET/POST、JSON、
超时、与 asyncio.gather 并发请求。

需先安装：pip install aiohttp

**说明**：示例会请求公网 `httpbin.org`；若本机无网络或对方不可达，会打印提示。
"""

from __future__ import annotations

import asyncio
import time

import aiohttp

HTTPBIN = "https://httpbin.org"
# 公网可能较慢，给整体请求设上限
TIMEOUT = aiohttp.ClientTimeout(total=20, connect=10)


# ---------------------------------------------------------------------------
# 1. GET + 查询参数
# ---------------------------------------------------------------------------


async def demo_get_querystring() -> None:
    url = f"{HTTPBIN}/get"
    async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
        async with session.get(url, params={"foo": "bar", "page": 1}) as resp:
            print("  状态码:", resp.status, resp.reason)
            data = await resp.json()
            print("  回显 query:", data.get("args"))


# ---------------------------------------------------------------------------
# 2. POST + JSON
# ---------------------------------------------------------------------------


async def demo_post_json() -> None:
    url = f"{HTTPBIN}/post"
    payload = {"user": "demo", "n": 42}
    async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
        async with session.post(url, json=payload) as resp:
            data = await resp.json()
            print("  对方收到的 JSON:", data.get("json"))


# ---------------------------------------------------------------------------
# 3. Session 级默认头
# ---------------------------------------------------------------------------


async def demo_session_headers() -> None:
    url = f"{HTTPBIN}/headers"
    headers = {"X-Demo": "aiohttp-示例", "User-Agent": "aiohttp-demo/1.0"}
    async with aiohttp.ClientSession(
        timeout=TIMEOUT, headers=headers
    ) as session:
        async with session.get(url) as resp:
            data = await resp.json()
            h = data.get("headers", {})
            print("  User-Agent 片段:", (h.get("User-Agent", "") or "")[:50], "…")


# ---------------------------------------------------------------------------
# 4. 同一 Session 上并发（gather）
# ---------------------------------------------------------------------------


async def _fetch_delay_status(session: aiohttp.ClientSession, name: str) -> str:
    url = f"{HTTPBIN}/delay/1"
    async with session.get(url) as resp:
        return f"{name}: 状态 {resp.status}"


async def demo_gather_concurrent() -> None:
    """三个请求各约 1s 延迟；并发执行，总耗时应明显小于 3s。"""
    t0 = time.perf_counter()
    async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
        results = await asyncio.gather(
            _fetch_delay_status(session, "A"),
            _fetch_delay_status(session, "B"),
            _fetch_delay_status(session, "C"),
        )
    elapsed = time.perf_counter() - t0
    for line in results:
        print(" ", line)
    # 若三个 delay/1 完全并行，总时间通常**接近 1s 档**；串行则约 3s+。实际会受网络与 httpbin 影响。
    print(f"  总耗时约 {elapsed:.2f}s（并发是「等最慢一个」，不是简单相加）")


# ---------------------------------------------------------------------------


async def main() -> None:
    demos = [
        ("=== 1. GET + query ===", demo_get_querystring),
        ("=== 2. POST json ===", demo_post_json),
        ("=== 3. Session 默认头 ===", demo_session_headers),
        ("=== 4. gather 并发（各 delay/1）===", demo_gather_concurrent),
    ]
    for title, fn in demos:
        print(title, flush=True)
        try:
            await fn()
        except (aiohttp.ClientError, TimeoutError, asyncio.TimeoutError) as e:
            print("  请求失败（检查网络/代理/防火墙）:", type(e).__name__, e)
        except OSError as e:  # 如连接被拒绝
            print("  网络层错误:", type(e).__name__, e)
        print()


if __name__ == "__main__":
    asyncio.run(main())
