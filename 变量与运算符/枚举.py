"""
标准库 enum 基础示例：Enum、IntEnum、IntFlag、@unique、auto、
比较与迭代。Python 3.10+ 含 match 示例。直接运行本文件会打印各节输出。

无需额外依赖。
"""

from __future__ import annotations

import enum
from enum import Enum, IntEnum, IntFlag, auto, unique


# ---------------------------------------------------------------------------
# 1. Enum：成员是单例，有 .name 与 .value
# ---------------------------------------------------------------------------


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def demo_enum_basic() -> None:
    c = Color.RED
    print("  成员:", c)
    print("  .name / .value:", c.name, c.value)
    print("  同一成员是单例:", Color.RED is Color["RED"] is Color(1) is c)
    # 按**值**用 Color(2)；按**成员名**用 Color['BLUE']（与 dict 键类似）
    print("  Color(2) ==", Color(2), "  Color['BLUE'] ==", Color["BLUE"])


# ---------------------------------------------------------------------------
# 2. IntEnum：可当作 int 使用（可比较、可参与与 int 的运算；勿滥用，可能模糊类型）
# ---------------------------------------------------------------------------


class Weekday(IntEnum):
    MONDAY = 1
    SUNDAY = 7


def demo_int_enum() -> None:
    print("  Weekday.MONDAY == 1 :", Weekday.MONDAY == 1)
    print("  Weekday.MONDAY + 1  :", Weekday.MONDAY + 1)
    print("  isinstance(Weekday.SUNDAY, int):", isinstance(Weekday.SUNDAY, int))


# ---------------------------------------------------------------------------
# 3. @unique：保证成员值不重复
# ---------------------------------------------------------------------------


@unique
class UniqueId(Enum):
    A = 1
    B = 2
    C = 3
    # 若 D = 1 则定义阶段会报 ValueError（重复值）


# ---------------------------------------------------------------------------
# 4. auto()：让解释器按顺序分配整数值（可配合 _ignore_ 等，此处略）
# ---------------------------------------------------------------------------


class TaskState(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()


def demo_auto() -> None:
    for s in TaskState:
        print(" ", s.name, "->", s.value)


# ---------------------------------------------------------------------------
# 5. IntFlag：位标志，可用 | 组合、& 判断、^ 切换
# ---------------------------------------------------------------------------


class Perm(IntFlag):
    READ = 1
    WRITE = 2
    EXEC = 4


def demo_intflag() -> None:
    p = Perm.READ | Perm.WRITE
    print("  READ | WRITE =", p, "value =", p.value)
    print("  含 READ?", bool(p & Perm.READ), " 含 EXEC?", bool(p & Perm.EXEC))


# ---------------------------------------------------------------------------
# 6. 迭代与 __members__
# ---------------------------------------------------------------------------


def demo_iter_members() -> None:
    print("  顺序迭代:", list(Color))
    print("  名称 -> 成员:", {name: m for name, m in Color.__members__.items()})


# ---------------------------------------------------------------------------
# 7. match / case（Python 3.10+）
# ---------------------------------------------------------------------------


def label_color(c: Color) -> str:
    match c:
        case Color.RED:
            return "红"
        case Color.GREEN:
            return "绿"
        case Color.BLUE:
            return "蓝"
        case _:
            return "其他"


# ---------------------------------------------------------------------------
# 8. StrEnum：成员值为 str，行为接近 str（Python 3.11+）
# ---------------------------------------------------------------------------


def demo_strenum_if_available() -> None:
    if hasattr(enum, "StrEnum"):

        class HttpError(enum.StrEnum):
            NOT_FOUND = "404"
            TEAPOT = "418"

        e = HttpError("404")
        print("  StrEnum 成员:", e, " 与 str 拼接:", f"code={e}")
    else:
        print("  当前解释器 < 3.11，无 StrEnum；略过")


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("=== 1. Enum 基本 ===", flush=True)
    demo_enum_basic()
    print()

    print("=== 2. IntEnum ===", flush=True)
    demo_int_enum()
    print()

    print("=== 3. @unique ===", flush=True)
    print("  UniqueId 在定义时即保证 A/B/C 值唯一（见类上方注释与源码）。")
    print()

    print("=== 4. auto() ===", flush=True)
    demo_auto()
    print()

    print("=== 5. IntFlag ===", flush=True)
    demo_intflag()
    print()

    print("=== 6. 迭代与 __members__ ===", flush=True)
    demo_iter_members()
    print()

    print("=== 7. match / case ===", flush=True)
    print("  label_color(Color.GREEN) ->", label_color(Color.GREEN))
    print()

    print("=== 8. StrEnum (3.11+) ===", flush=True)
    demo_strenum_if_available()
