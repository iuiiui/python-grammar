"""
FastAPI Web 框架示例

需先安装：
    pip install fastapi uvicorn

运行方式：
    python -m uvicorn "web框架.FastAPI  web框架:app" --reload

如果已经进入 web框架 目录，运行：
    python -m uvicorn "FastAPI  web框架:app" --reload

说明：
    如果直接执行 uvicorn 提示“无法将 uvicorn 项识别为 cmdlet”，说明 uvicorn.exe
    没有加入 PATH；用 python -m uvicorn 可以直接调用当前 Python 环境中的模块。

访问地址：
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/api/todos
"""

from __future__ import annotations

from typing import Annotated

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="FastAPI 教学示例",
    description="演示路由、查询参数、路径参数、请求体、响应模型和异常处理。",
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# 1. Pydantic 数据模型：声明请求体和响应结构
# ---------------------------------------------------------------------------

class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100, examples=["学习 FastAPI"])
    done: bool = False


class Todo(TodoCreate):
    id: int


# ---------------------------------------------------------------------------
# 2. 模拟数据库：实际项目中通常替换为数据库或 ORM
# ---------------------------------------------------------------------------

todos: list[Todo] = [
    Todo(id=1, title="理解路径参数", done=True),
    Todo(id=2, title="使用查询参数过滤数据", done=False),
    Todo(id=3, title="定义请求体模型", done=False),
]


def find_todo(todo_id: int) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="待办不存在",
    )


# ---------------------------------------------------------------------------
# 3. 路由示例：装饰器中的路径和方法决定接口形式
# ---------------------------------------------------------------------------

@app.get("/")
def index() -> dict[str, str]:
    return {
        "message": "FastAPI 单文件示例",
        "docs": "打开 /docs 查看自动生成的 Swagger 文档",
    }


@app.get("/api/todos", response_model=list[Todo])
def list_todos(
    done: Annotated[bool | None, Query(description="按完成状态过滤")] = None,
) -> list[Todo]:
    if done is None:
        return todos
    return [todo for todo in todos if todo.done is done]


@app.get("/api/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    return find_todo(todo_id)


@app.post(
    "/api/todos",
    response_model=Todo,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(payload: TodoCreate) -> Todo:
    next_id = max((todo.id for todo in todos), default=0) + 1
    todo = Todo(id=next_id, title=payload.title, done=payload.done)
    todos.append(todo)
    return todo


@app.put("/api/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoCreate) -> Todo:
    todo = find_todo(todo_id)
    updated = Todo(id=todo.id, title=payload.title, done=payload.done)
    index = todos.index(todo)
    todos[index] = updated
    return updated


@app.delete("/api/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int) -> None:
    todo = find_todo(todo_id)
    todos.remove(todo)
    return None


# ---------------------------------------------------------------------------
# 4. 常规项目写法参考
# ---------------------------------------------------------------------------

"""
常规 FastAPI 项目结构示例：

my_fastapi_project/
├── main.py
├── routers/
│   └── todos.py
├── schemas/
│   └── todo.py
└── services/
    └── todo_service.py

main.py：
    from fastapi import FastAPI
    from routers import todos

    app = FastAPI()
    app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

routers/todos.py：
    from fastapi import APIRouter

    router = APIRouter()

    @router.get("/")
    def list_todos():
        return []

启动命令：
    python -m uvicorn main:app --reload

FastAPI 特点：
    1. 基于类型注解自动校验请求参数
    2. 自动生成 /docs 和 /redoc 接口文档
    3. 原生支持 async def 异步接口
    4. 常与 Pydantic、SQLAlchemy、SQLModel 搭配使用
"""
