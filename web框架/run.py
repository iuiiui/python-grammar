"""本地开发入口：在本目录执行 ``pip install -r requirements.txt`` 后 ``python run.py``。

环境变量：``FLASK_RUN_HOST``（默认 127.0.0.1）、``FLASK_RUN_PORT``（默认 5500，避开常被向日葵等占用的 5000）。
HTTPS / localhost→IPv6 / 端口冲突导致加载异常时，改用 ``http://127.0.0.1:<端口>``。
"""

import os

from apps import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True 下默认 use_reloader=True；Windows 上偶发卡请求，此处显式关掉。
    port = int(os.environ.get("FLASK_RUN_PORT", "5500"))
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    print(f"\n→ http://{host}:{port}/\n")

    app.run(
        host=host,
        port=port,
        debug=True,
        use_reloader=False,
        threaded=True,
    )
