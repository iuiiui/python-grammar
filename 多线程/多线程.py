"""
多线程（threading）基础示例：Thread、start/join、守护线程、Lock、Queue、
以及 concurrent.futures 线程池的简要对比。

说明（CPython）：受 GIL 影响，**多线程**对 **I/O 等待**（网络、磁盘）能重叠等待时间；
**纯 CPU 密集**计算用多进程（multiprocessing）往往更合适。这里只演示 API 用法。

直接运行本文件会顺序执行各 demo 并打印输出。
"""

from __future__ import annotations

import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# ---------------------------------------------------------------------------
# 1. 基本：Thread、start、join
# ---------------------------------------------------------------------------


def _worker_say(name: str, delay: float) -> None:
    time.sleep(delay)
    print(f"[{name}] 完成")


def demo_thread_basic() -> None:
    t1 = threading.Thread(target=_worker_say, args=("线程 A", 0.05))
    t2 = threading.Thread(target=_worker_say, kwargs={"name": "线程 B", "delay": 0.05})
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程：子线程已 join 完毕")


# ---------------------------------------------------------------------------
# 2. 守护线程 daemon：主程序退出时不等待其结束（适合后台任务，慎用）
# ---------------------------------------------------------------------------


def demo_daemon() -> None:
    def background() -> None:
        time.sleep(0.3)
        print("这行在 daemon 中，主线程若已退出，可能**看不到**")

    d = threading.Thread(target=background, daemon=True, name="后台")
    d.start()
    # 不 join：主线程很快结束，进程可能直接结束，子线程或来不及打印
    print("主线程：启动 daemon 后立即继续（不等待）")


# ---------------------------------------------------------------------------
# 3. Lock：互斥，保护共享数据
# ---------------------------------------------------------------------------


def demo_lock() -> None:
    lock = threading.Lock()
    counter = 0
    n_iter = 100_000

    def bump() -> None:
        nonlocal counter
        for _ in range(n_iter):
            with lock:
                counter += 1

    t1 = threading.Thread(target=bump)
    t2 = threading.Thread(target=bump)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    assert counter == 2 * n_iter
    print("加锁后 counter =", counter, "（若去掉 lock，结果可能小于预期）")


# ---------------------------------------------------------------------------
# 4. queue.Queue：线程间安全传数据（内部已加锁）
# ---------------------------------------------------------------------------


def demo_queue() -> None:
    q: queue.Queue[str] = queue.Queue()

    def producer() -> None:
        for s in ("a", "b", "c"):
            q.put(s)
        q.put(None)  # 结束哨兵

    def consumer() -> None:
        while True:
            item = q.get()
            if item is None:
                q.task_done()
                break
            print("  取到:", item)
            q.task_done()

    t_prod = threading.Thread(target=producer)
    t_cons = threading.Thread(target=consumer)
    t_prod.start()
    t_cons.start()
    t_prod.join()
    t_cons.join()


# ---------------------------------------------------------------------------
# 5. ThreadPoolExecutor：池化线程，适合「一批可调用对象」
# ---------------------------------------------------------------------------


def _square(n: int) -> int:
    time.sleep(0.02)
    return n * n


def demo_thread_pool() -> None:
    nums = (1, 2, 3, 4, 5)
    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = [ex.submit(_square, n) for n in nums]
        for fut in as_completed(futures):
            print("  结果:", fut.result())
    print("with 块结束，线程池已关闭")


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("=== 1. 基本 start / join ===")
    demo_thread_basic()
    time.sleep(0.15)
    print()

    print("=== 2. daemon（主线程不等待；输出可能截断）===")
    demo_daemon()
    time.sleep(0.35)
    print()

    print("=== 3. Lock 累加 ===")
    demo_lock()
    print()

    print("=== 4. Queue 生产者/消费者 ===")
    demo_queue()
    print()

    print("=== 5. ThreadPoolExecutor ===")
    demo_thread_pool()
