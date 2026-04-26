"""
可迭代对象（iterable）与迭代器（iterator）、生成器（generator）相关示例。

- 可迭代：能用 for 遍历，或交给 iter()，通常实现 __iter__ 返回迭代器。
- 迭代器：实现 __next__（旧式 __next__ 在 Py2 为 next），无更多元素时抛 StopIteration，通常也实现 __iter__ 返回自身。
- 生成器：含 yield 的函数，或生成器表达式；是一种便捷的迭代器实现。

直接运行本文件会打印各示例输出。
"""

from __future__ import annotations

import itertools


# ---------------------------------------------------------------------------
# 1. 可迭代与迭代器：iter / next
# ---------------------------------------------------------------------------


def demo_iter_next() -> None:
    it = iter([1, 2, 3])
    print(next(it), next(it), next(it))
    try:
        next(it)
    except StopIteration as e:
        print("迭代结束:", type(e).__name__, "value 无值" if e.value is None else e.value)


# ---------------------------------------------------------------------------
# 2. 自定义迭代器类：__iter__ + __next__
# ---------------------------------------------------------------------------


class Countdown:
    """从 n 数到 1 的简单迭代器。"""

    def __init__(self, start: int) -> None:
        if start < 1:
            raise ValueError("start 应为正整数")
        self._n = start

    def __iter__(self) -> Countdown:
        return self

    def __next__(self) -> int:
        if self._n == 0:
            raise StopIteration
        self._n -= 1
        return self._n + 1


# ---------------------------------------------------------------------------
# 3. 生成器函数：yield
# ---------------------------------------------------------------------------


def count_up_to(n: int):
    """每步 yield 一个数，状态保存在生成器对象里。"""
    k = 1
    while k <= n:
        yield k
        k += 1


# ---------------------------------------------------------------------------
# 4. 生成器表达式（与列表推导形式类似，但惰性求值）
# ---------------------------------------------------------------------------


def demo_genexpr() -> None:
    g = (x * x for x in range(1, 4))
    print("生成器对象:", g)
    print("转列表（会消耗迭代器）:", list(g))
    h = (x for x in range(3))
    print("逐个 next:", next(h), next(h), next(h))


# ---------------------------------------------------------------------------
# 5. yield from：把迭代工作委托给另一个可迭代对象
# ---------------------------------------------------------------------------


def flatten(nested: list[list[int]]):
    for sub in nested:
        yield from sub


# ---------------------------------------------------------------------------
# 6. 生成器：send / throw / close（协程前身的典型用法，了解即可）
# ---------------------------------------------------------------------------


def echo_generator():
    """先 yield 启动，再接收外界 send 的值并回显。"""
    n = None
    while True:
        n = yield n
        if n is None:
            break


def demo_send_close() -> None:
    g = echo_generator()
    next(g)  # 预激到第一个 yield
    print("send(10):", g.send(10))
    g.close()  # 引发 GeneratorExit，生成器结束


# ---------------------------------------------------------------------------
# 7. itertools 一瞥：无限与组合迭代（惰性）
# ---------------------------------------------------------------------------


def demo_itertools_sample() -> None:
    c = itertools.count(10, step=2)
    print("itertools.count 前 3 个:", [next(c), next(c), next(c)])
    cy = itertools.cycle("ab")
    print("itertools.cycle 前 5 个:", [next(cy) for _ in range(5)])


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("=== 1. iter / next ===")
    demo_iter_next()
    print()

    print("=== 2. 自定义迭代器 Countdown(3) ===")
    for x in Countdown(3):
        print(x, end=" ")
    print()
    print()

    print("=== 3. 生成器函数 count_up_to(3) ===")
    g = count_up_to(3)
    print("生成器是迭代器的一种:", g)
    print(list(g))
    print()

    print("=== 4. 生成器表达式 ===")
    demo_genexpr()
    print()

    print("=== 5. yield from flatten ===")
    print(list(flatten([[1, 2], [3], [4, 5]])))
    print()

    print("=== 6. send / close ===")
    demo_send_close()
    print()

    print("=== 7. itertools 示例 ===")
    demo_itertools_sample()
