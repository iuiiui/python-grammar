"""
流程控制之「循环」：for、while、break、continue、for/while 的 else 子句、
range、enumerate、zip 与简单嵌套循环。直接运行本文件会打印各示例输出。
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# 1. for：遍历可迭代对象
# ---------------------------------------------------------------------------


def demo_for_basic() -> None:
    for ch in "abc":
        print(ch, end=" ")
    print()

    for n in (1, 2, 3):
        print(n, end=" ")
    print()


# ---------------------------------------------------------------------------
# 2. range：整数序列，常与 for 配合
# ---------------------------------------------------------------------------


def demo_range() -> None:
    # range(stop)：0 到 stop-1
    print("range(3):", list(range(3)))
    # range(start, stop)
    print("range(2, 5):", list(range(2, 5)))
    # range(start, stop, step)，step 可正可负
    print("range(0, 10, 3):", list(range(0, 10, 3)))
    print("range(5, 0, -1):", list(range(5, 0, -1)))


# ---------------------------------------------------------------------------
# 3. while：条件为真则重复
# ---------------------------------------------------------------------------


def demo_while() -> None:
    n = 3
    while n > 0:
        print("n =", n)
        n -= 1


# ---------------------------------------------------------------------------
# 4. break：跳出**当前**循环；continue：跳过本轮余下语句进入下一轮
# ---------------------------------------------------------------------------


def demo_break_continue() -> None:
    for i in range(6):
        if i == 2:
            continue
        if i == 4:
            break
        print(i, end=" ")
    print("（在 i==4 时 break，故不会打印 4、5）")


# ---------------------------------------------------------------------------
# 5. for-else / while-else：循环**正常跑完**（未因 break 退出）时执行 else
# ---------------------------------------------------------------------------


def demo_for_else() -> None:
    for i in (1, 2, 3):
        if i == 10:
            break
    else:
        print("for 未 break，执行 else：上面序列里没有 10")

    for i in (1, 2, 3):
        if i == 2:
            break
    else:
        print("这行不会执行，因为被 break 了")


# ---------------------------------------------------------------------------
# 6. enumerate：同时需要下标和元素
# ---------------------------------------------------------------------------


def demo_enumerate() -> None:
    items = ["a", "b", "c"]
    for index, value in enumerate(items, start=0):
        print(index, value)


# ---------------------------------------------------------------------------
# 7. zip：并行迭代多个可迭代对象，长度以**最短**为准
# ---------------------------------------------------------------------------


def demo_zip() -> None:
    names = ("甲", "乙", "丙")
    ages = (20, 30)
    for name, age in zip(names, ages):
        print(name, age)
    # Python 3.10+ 可用 zip(..., strict=True) 在长度不等时抛 ValueError


# ---------------------------------------------------------------------------
# 8. 嵌套循环：内层 break 只结束内层
# ---------------------------------------------------------------------------


def demo_nested() -> None:
    for i in range(2):
        for j in range(2):
            print(f"({i},{j})", end=" ")
        print()


# ---------------------------------------------------------------------------
# 9. 列表推导（与 for 同语法思想，产生新列表）
# ---------------------------------------------------------------------------


def demo_list_comprehension() -> None:
    squares = [x * x for x in range(1, 4)]
    print("squares:", squares)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("=== 1. for 基本 ===")
    demo_for_basic()
    print()

    print("=== 2. range ===")
    demo_range()
    print()

    print("=== 3. while ===")
    demo_while()
    print()

    print("=== 4. break / continue ===")
    demo_break_continue()
    print()

    print("=== 5. for-else ===")
    demo_for_else()
    print()

    print("=== 6. enumerate ===")
    demo_enumerate()
    print()

    print("=== 7. zip ===")
    demo_zip()
    print()

    print("=== 8. 嵌套 ===")
    demo_nested()
    print()

    print("=== 9. 列表推导 ===")
    demo_list_comprehension()
