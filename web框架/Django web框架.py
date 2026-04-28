"""
Django Web 框架单文件示例

需先安装：pip install django

运行方式：
    python "Django web框架.py" runserver 127.0.0.1:8000

访问地址：
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/api/todos/
    http://127.0.0.1:8000/api/todos/1/

Django 正常项目通常会拆成 manage.py、settings.py、urls.py、views.py、
models.py 等文件。这里为了便于学习，把 settings、路由和视图放在同一个
Python 文件中演示核心概念。
"""

from __future__ import annotations

import os
import sys
from typing import Any

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def configure_django() -> None:
    """单文件运行时手动配置 Django 项目设置。"""
    if settings.configured:
        return

    settings.configure(
        DEBUG=True,
        SECRET_KEY="django-single-file-demo",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["127.0.0.1", "localhost"],
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
        ],
        MIDDLEWARE=[],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {"context_processors": []},
            }
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "django_demo.sqlite3"),
            }
        },
    )


# ---------------------------------------------------------------------------
# 1. 模拟数据：实际项目中通常放在 models.py，并通过 ORM 操作数据库
# ---------------------------------------------------------------------------

TODOS: list[dict[str, Any]] = [
    {"id": 1, "title": "学习 Django 路由", "done": True},
    {"id": 2, "title": "编写视图函数", "done": False},
    {"id": 3, "title": "返回 JSON 响应", "done": False},
]


# ---------------------------------------------------------------------------
# 2. 视图函数：接收 HttpRequest，返回 HttpResponse 或 JsonResponse
# ---------------------------------------------------------------------------

def index(request: HttpRequest) -> HttpResponse:
    html = """
    <h1>Django 单文件示例</h1>
    <p>这是一个最小 Django Web 应用。</p>
    <ul>
        <li><a href="/api/todos/">查看待办列表 JSON</a></li>
        <li><a href="/api/todos/1/">查看 ID=1 的待办</a></li>
    </ul>
    """
    return HttpResponse(html)


def todo_list(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse({"error": "只支持 GET 请求"}, status=405)

    only_done = request.GET.get("done")
    data = TODOS
    if only_done == "true":
        data = [todo for todo in TODOS if todo["done"]]
    elif only_done == "false":
        data = [todo for todo in TODOS if not todo["done"]]

    return JsonResponse({"count": len(data), "results": data})


def todo_detail(request: HttpRequest, todo_id: int) -> JsonResponse:
    for todo in TODOS:
        if todo["id"] == todo_id:
            return JsonResponse(todo)
    return JsonResponse({"error": "待办不存在"}, status=404)


# ---------------------------------------------------------------------------
# 3. URL 路由：把访问路径映射到视图函数
# ---------------------------------------------------------------------------

urlpatterns = [
    path("", index),
    path("api/todos/", todo_list),
    path("api/todos/<int:todo_id>/", todo_detail),
]


# ---------------------------------------------------------------------------
# 4. 常规项目写法参考
# ---------------------------------------------------------------------------

"""
常规 Django 项目结构示例：

my_django_project/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── todos/
    ├── models.py
    ├── views.py
    └── urls.py

常用命令：
    django-admin startproject config .
    python manage.py startapp todos
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

典型 models.py：
    from django.db import models

    class Todo(models.Model):
        title = models.CharField(max_length=100)
        done = models.BooleanField(default=False)

典型 views.py：
    from django.http import JsonResponse
    from .models import Todo

    def todo_list(request):
        data = list(Todo.objects.values("id", "title", "done"))
        return JsonResponse({"results": data})
"""


if __name__ == "__main__":
    configure_django()
    execute_from_command_line(sys.argv)
