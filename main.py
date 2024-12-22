from fastapi import FastAPI
from routers.user import router as user_router
from routers.task import router as task_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутов
app.include_router(user_router)
app.include_router(task_router)
