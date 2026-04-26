"""
asyncio 基础示例：协程（async def）、事件循环、并发等待 gather、
Task、asyncio.sleep、阻塞调用的 to_thread 等。

**概念**：`asyncio` 在**单线程**里用「协作式多任务」切换协程，适合 I/O 密集；
与「多线程/多进程」是不同维度的工具，常组合使用（例如用线程跑阻塞库）。

在 Python 3.7+ 中，用 `asyncio.run(main())` 启动。直接运行本文件会顺序执行各 demo。
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Coroutine
from typing import Any


# ---------------------------------------------------------------------------
# 1. async / await 与事件循环
# ---------------------------------------------------------------------------


async def demo_hello() -> None:
    print("  协程内：即将 await asyncio.sleep(0.05)")
    await asyncio.sleep(0.05)
    print("  协程内：sleep 结束")


# ---------------------------------------------------------------------------
# 2. asyncio.gather：并发运行多个协程，按入参顺序汇总结果
# ---------------------------------------------------------------------------


async def _add_delay(value: int, delay: float) -> int:
    await asyncio.sleep(delay)
    return value * 10


async def demo_gather() -> None:
    t0 = time.perf_counter()
    a, b, c = await asyncio.gather(
        _add_delay(1, 0.05),
        _add_delay(2, 0.05),
        _add_delay(3, 0.05),
    )
    elapsed = time.perf_counter() - t0
    print("  结果:", a, b, c, f"（总耗时约 {elapsed:.3f}s，三次睡眠重叠而非相加）")


# ---------------------------------------------------------------------------
# 3. create_task：调度协程，稍后 await 或后台运行
# ---------------------------------------------------------------------------


async def demo_create_task() -> None:
    async def tick(name: str) -> None:
        for i in range(2):
            print(f"    [{name}] {i}")
            await asyncio.sleep(0.02)

    t1 = asyncio.create_task(tick("A"))
    t2 = asyncio.create_task(tick("B"))
    await t1
    await t2


# ---------------------------------------------------------------------------
# 4. wait_for 超时
# ---------------------------------------------------------------------------


async def demo_wait_for() -> None:
    async def slow() -> str:
        await asyncio.sleep(1.0)
        return "ok"

    try:
        _ = await asyncio.wait_for(slow(), timeout=0.1)
    except TimeoutError:
        print("  wait_for 在 0.1s 超时，已取消 slow()")


# ---------------------------------------------------------------------------
# 5. gather 与 return_exceptions
# ---------------------------------------------------------------------------


async def demo_gather_exceptions() -> None:
    async def raises() -> None:
        raise ValueError("演示用")

    r1, r2 = await asyncio.gather(
        asyncio.sleep(0, result="正常"),
        raises(),
        return_exceptions=True,
    )
    print("  第一个结果:", r1)
    print("  第二个是异常对象:", r2, type(r2).__name__)


# ---------------------------------------------------------------------------
# 6. asyncio.to_thread：在线程中跑**阻塞**函数，避免卡死事件循环
#     （需 Python 3.9+；更旧版可用 loop.run_in_executor）
# ---------------------------------------------------------------------------


def _blocking_io() -> str:
    time.sleep(0.08)  # 同步阻塞
    return "阻塞结束"


async def demo_to_thread() -> None:
    s = await asyncio.to_thread(_blocking_io)
    print("  在线程中完成:", s)


# ---------------------------------------------------------------------------
# 7. asyncio.Lock：协程间互斥（同一事件循环内）
# ---------------------------------------------------------------------------


async def demo_async_lock() -> None:
    lock = asyncio.Lock()
    counter = 0

    async def bump() -> None:
        nonlocal counter
        for _ in range(1000):
            async with lock:
                counter += 1

    await asyncio.gather(bump(), bump())
    assert counter == 2000
    print("  加锁后 counter =", counter)


# ---------------------------------------------------------------------------


def _run_section(title: str, coro: Coroutine[Any, Any, None]) -> None:
    print(title, flush=True)
    asyncio.run(coro)
    print()


if __name__ == "__main__":
    _run_section("=== 1. async / await + asyncio.sleep ===", demo_hello())
    _run_section("=== 2. asyncio.gather 并发 ===", demo_gather())
    _run_section("=== 3. create_task ===", demo_create_task())
    _run_section("=== 4. wait_for 超时 ===", demo_wait_for())
    _run_section("=== 5. gather + return_exceptions ===", demo_gather_exceptions())
    _run_section("=== 6. asyncio.to_thread ===", demo_to_thread())
    _run_section("=== 7. asyncio.Lock ===", demo_async_lock())
