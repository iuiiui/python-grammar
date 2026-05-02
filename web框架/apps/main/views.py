"""首页与健康检查蓝图。"""
from typing import Literal

from flask import Blueprint, Response, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index() -> str:
    return (
        "<p>Flask 标准示例（应用工厂 + 蓝图）</p>"
        "<ul>"
        '<li><a href="/health">/health</a></li>'
        '<li><a href="/api/user/info">/api/user/info</a></li>'
        "</ul>"
    )


@main_bp.route("/health")
def health() -> tuple[Response, Literal[200]]:
    return jsonify({"status": "ok"}), 200
