"""部署 WSGI 入口：例如 ``gunicorn 'wsgi:app'`` / ``waitress-serve wsgi:app``（模块名勿带 .py）。"""

from apps import create_app

app = create_app(config_name="production")
