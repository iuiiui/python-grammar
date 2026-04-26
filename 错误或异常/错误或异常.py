"""
Python 中「错误」与「异常」相关示例：语法/逻辑错误、常见内置异常、捕获与处理、抛出、自定义异常。
直接运行本文件会依次执行各 demo 中的说明性代码（部分故意触发异常，由 try/except 接住）。
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# 1. 错误类型简述
# ---------------------------------------------------------------------------
# - 语法错误 (SyntaxError)：代码不符合 Python 语法，解释器在解析阶段就失败，无法用 try/except 捕获同一段「错误源码」的解析。
# - 异常 (Exception)：运行期问题，如除零、键不存在、类型错误等，可被 try/except 处理。


def demo_syntax_error_explanation() -> None:
    """说明：下面若去掉注释，运行时会先报 SyntaxError，整段不会进入 try。"""
    # eval("1 + + 1")  # SyntaxError
    pass


# ---------------------------------------------------------------------------
# 2. 常见内置异常（示意）
# ---------------------------------------------------------------------------


def demo_common_builtin_exceptions() -> None:
    examples: list[tuple[str, str]] = [
        ("ZeroDivisionError", "1 / 0"),
        ("NameError", "undefined_name_xyz"),
        ("TypeError", "'a' + 1"),
        ("ValueError", "int('不是数字')"),
        ("KeyError", "{'a': 1}['b']"),
        ("IndexError", "[0, 1][10]"),
        ("AttributeError", "''.missing_attr"),
    ]

    for name, code in examples:
        try:
            exec(code, {"__builtins__": __builtins__}, {})
        except Exception as e:  # noqa: BLE001 教学示例，展示多种类型
            print(f"{name}: 实际类型为 {type(e).__name__} -> {e!r}")


# ---------------------------------------------------------------------------
# 3. try / except / else / finally
# ---------------------------------------------------------------------------


def safe_divide(a: float, b: float) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为 0。")
        return None
    else:
        # 无异常时执行
        return result
    finally:
        # 无论是否异常都会执行，常用于释放资源
        pass


# ---------------------------------------------------------------------------
# 4. 捕获多种异常 与 获取异常信息
# ---------------------------------------------------------------------------


def demo_multiple_except() -> None:
    for value in (10, 0, "x"):
        try:
            y = 1 / int(value)  # type: ignore[arg-type]
            print(f"1 / {value} = {y}")
        except (ZeroDivisionError, ValueError) as e:
            print(f"无法计算 value={value!r}：{e}")
        except TypeError as e:
            print(f"类型问题：{e}")


# ---------------------------------------------------------------------------
# 5. 重新抛出 与 异常链
# ---------------------------------------------------------------------------


def load_config_key(data: dict[str, str], key: str) -> str:
    try:
        return data[key]
    except KeyError as e:
        raise ValueError(f"配置缺少键 {key!r}") from e


# ---------------------------------------------------------------------------
# 6. 主动抛出：raise
# ---------------------------------------------------------------------------


def ensure_positive(n: int) -> None:
    if n <= 0:
        raise ValueError("n 必须为正整数")


# ---------------------------------------------------------------------------
# 7. 自定义异常
# ---------------------------------------------------------------------------


class BusinessRuleError(Exception):
    """业务规则不满足。"""

    def __init__(self, message: str, code: str = "RULE") -> None:
        super().__init__(message)
        self.code = code


def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise BusinessRuleError("余额不足", code="INSUFFICIENT_FUNDS")
    return balance - amount


# ---------------------------------------------------------------------------
# 8. assert（仅用于开发期、不应依赖它处理用户输入）
# ---------------------------------------------------------------------------


def demo_assert() -> None:
    x = 1
    assert x > 0, "x 应大于 0"  # 为 False 时引发 AssertionError


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("=== 2. 常见内置异常 ===")
    demo_common_builtin_exceptions()
    print()

    print("=== 3. safe_divide ===")
    print("safe_divide(10, 2) =", safe_divide(10, 2))
    print("safe_divide(1, 0) =", safe_divide(1, 0))
    print()

    print("=== 4. 多种 except ===")
    demo_multiple_except()
    print()

    print("=== 5. 异常链 ===")
    try:
        _ = load_config_key({}, "user")
    except ValueError as e:
        print("捕获:", e)
        print("__cause__:", e.__cause__)
    print()

    print("=== 6. ensure_positive(0) ===")
    try:
        ensure_positive(0)
    except ValueError as e:
        print(e)
    print()

    print("=== 7. withdraw 余额不足 ===")
    try:
        _ = withdraw(100, 200)
    except BusinessRuleError as e:
        print(e, e.code)
    print()

    print("=== 8. assert ===")
    demo_assert()
