"""用户模块蓝图（示例 JSON）。前缀 /api/user 在 create_app 中注册。"""
from typing import Literal

from flask import Blueprint, Response, jsonify

user_bp = Blueprint("user", __name__)


@user_bp.route("/info")
def info() -> tuple[Response, Literal[200]]:
    return jsonify({"module": "user", "demo": True}), 200
