from ninja import NinjaAPI, Schema
from typing import List 
from .models import Todo 
from django.shortcuts import get_object_or_404
from datetime import datetime #과제 : datetime 모듈 안의 datetime class를 불러와야 함, 각 필드의 타입을 명확하기 하기 위해서 class를 불러와야 함

api = NinjaAPI()

class TodoSchema(Schema):
    id: int 
    title: str 
    completed: bool 
    due_date: datetime # 과제 : models.py에서 models.DateTimeField()로 선언

class TodoIn(Schema):
    title: str 
    completed: bool = False 
    due_date: datetime # 과제 : models.py에서 models.DateTimeField()로 선언


# --- GET Endpoints ---

# 첫 번째 API 엔드포인트 (GET /hello)
@api.get("/hello")
def hello(request):
    return {"message": "Hello, Ninja!"}

# 모든 할 일 목록 가져오기
@api.get("/todos", response=List[TodoSchema]) 
def list_todos(request):
    todos = Todo.objects.all()
    return todos 

# 특정 할 일 하나 가져오기 (ID로 구분)
@api.get("/todos/{todo_id}", response=TodoSchema) 
def get_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    return todo

# --- POST Endpoint (할 일 생성) ---
@api.post("/todos", response=TodoSchema)
def create_todo(request, todo_in: TodoIn):
    todo = Todo.objects.create(**todo_in.dict())
    return todo 

# --- PUT/PATCH Endpoint (할 일 수정) ---
@api.put("/todos/{todo_id}", response=TodoSchema)
def update_todo(request, todo_id: int, todo_in: TodoIn):
    todo = get_object_or_404(Todo, id=todo_id)
    # todo_in.dict() 의 내용을 todo 객체에 업데이트
    for key, value in todo_in.dict().items():
        setattr(todo, key, value)
    todo.save() 
    return todo 


# --- DELETE Endpoint (할 일 삭제) ---
@api.delete("/todos/{todo_id}")
def delete_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()