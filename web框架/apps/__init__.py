"""应用工厂：注册配置与蓝图。"""

from __future__ import annotations

import os

from flask import Flask

from apps.main.views import main_bp
from apps.user.views import user_bp
from config import DevelopmentConfig, config_by_name


def create_app(config_name: str | None = None) -> Flask:
    """config_name / FLASK_ENV → 配置类；缺省 development。"""
    app = Flask(__name__)

    name = config_name or os.environ.get("FLASK_ENV", "development")
    cfg = config_by_name.get(name, DevelopmentConfig)
    app.config.from_object(cfg)

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix="/api/user")

    return app
