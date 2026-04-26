"""
标准库 logging 基础示例：级别、记录器、处理器、格式、
父子记录器、异常栈，以及 dictConfig 简要说明。

**说明**：`basicConfig` 在进程里通常只配置一次；示例用 `force=True`（需 Python 3.8+）
在脚本内反复演示时可覆盖根记录器。直接运行本文件会打印/生成临时日志文件后删除。

无需额外依赖。
"""

from __future__ import annotations

import json
import logging
import logging.config
import os
import sys
import tempfile
from typing import NoReturn


# ---------------------------------------------------------------------------
# 1. 根记录器 + basicConfig + 各级别
# ---------------------------------------------------------------------------


def demo_levels() -> None:
    # 用 stdout 与下方 print 同一流，避免 Windows 上 stderr/stdout 交错
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
        force=True,
    )
    print("  （应看到 DEBUG 起全部级别）", flush=True)
    logging.debug("调试信息")
    logging.info("一般信息")
    logging.warning("警告")
    logging.error("错误")
    logging.critical("严重")


# ---------------------------------------------------------------------------
# 2. 具名记录器、父子、propagate
# ---------------------------------------------------------------------------


def demo_logger_hierarchy() -> None:
    """具名子记录器会出现在 `%(name)s` 里，形成 app / app.ui 等命名空间。"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
        force=True,
    )
    logging.getLogger("app").info("模块 app：info")
    logging.getLogger("app.ui").info("子模块 app.ui：info")
    logging.getLogger("app").warning("同模块的 warning，便于在日志中过滤 app.*")


# ---------------------------------------------------------------------------
# 3. Formatter + StreamHandler + FileHandler
# ---------------------------------------------------------------------------


def demo_handlers() -> None:
    logger = logging.getLogger("filedemo")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    fmt = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | [%(funcName)s:%(lineno)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    sh = logging.StreamHandler(stream=sys.stdout)
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(fmt)

    fd, path = tempfile.mkstemp(prefix="logging_demo_", suffix=".log")
    os.close(fd)
    fh = logging.FileHandler(path, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    logger.addHandler(sh)
    logger.addHandler(fh)
    # 不设 propagate，避免同一条再经根上重复
    logger.propagate = False

    logger.info("只打到控制台+文件")
    logger.debug("只打到控制台（FileHandler=INFO）")
    try:
        with open(path, encoding="utf-8") as f:
            line = f.readline().strip()
        print("  文件首行（节选）:", line[:100], "…" if len(line) > 100 else "")
    finally:
        fh.close()
        logger.removeHandler(fh)
        os.unlink(path)
    sh.close()
    logger.removeHandler(sh)


# ---------------------------------------------------------------------------
# 4. 异常时记录堆栈：logger.exception
# ---------------------------------------------------------------------------


def _maybe_raise() -> NoReturn:
    raise ValueError("演示异常")


def demo_exception() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)-8s | %(message)s",
        stream=sys.stdout,
        force=True,
    )
    log = logging.getLogger("exc")
    try:
        _maybe_raise()
    except ValueError:
        log.exception("捕获到了 ValueError，会附带 traceback：")


# ---------------------------------------------------------------------------
# 5. dictConfig：用字典集中配置（实际项目可来自 YAML/JSON 文件）
# ---------------------------------------------------------------------------


def demo_dictconfig() -> None:
    with tempfile.TemporaryDirectory() as d:
        log_path = os.path.join(d, "app.log")
        cfg: dict = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "std": {
                    "format": "%(levelname)s | %(name)s | %(message)s",
                }
            },
            "handlers": {
                "out": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "std",
                    "level": "DEBUG",
                },
                "f": {
                    "class": "logging.FileHandler",
                    "filename": log_path,
                    "encoding": "utf-8",
                    "formatter": "std",
                    "level": "DEBUG",
                },
            },
            "loggers": {
                "dictcfg": {
                    "level": "DEBUG",
                    "handlers": ["out", "f"],
                    "propagate": False,
                }
            },
        }
        logging.config.dictConfig(cfg)
        lg = logging.getLogger("dictcfg")
        lg.debug("到文件+控制台都可能有（handler 级过滤）")
        with open(log_path, encoding="utf-8") as f:
            content = f.read()
        print("  文件内容行数（含换行）:", content.count("\n") + 1)
        # 关闭 dictConfig 里创建的 FileHandler，否则 Windows 上临时目录无法删除
        logging.shutdown()
    print("  dictConfig 示例中临时目录已删；配置可用 JSON 从文件读：")
    print("  ", json.dumps({"version": 1, "keys": "handlers/formatters/loggers/..."}, ensure_ascii=False))


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("=== 1. 级别 + basicConfig ===", flush=True)
    demo_levels()
    print()

    print("=== 2. 记录器树 ===", flush=True)
    demo_logger_hierarchy()
    print()

    print("=== 3. StreamHandler + FileHandler ===", flush=True)
    demo_handlers()
    print()

    print("=== 4. exception ===", flush=True)
    demo_exception()
    print()

    print("=== 5. dictConfig ===", flush=True)
    demo_dictconfig()
