from sys import prefix
from fastapi import FastAPI
from fastapi.routing import APIRoute

from presentation.api.fastapi.controllers.task_controller import router as task_router
from presentation.api.fastapi.controllers.auth_controller import router as auth_router

app = FastAPI(
    debug=True,
    docs_url="/docs",
    redoc_url="/redoc",
    title="Task Management API",
    description="API for managing tasks using Clean Architecture",
    version="1.0.0",
    contact={
        "name": "Fatemeh Ahmadzadeh",
        "email": "ahmadzade920@gmail.com"
    }
   
)

app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
def _root():
    routes = []
    for route in app.routes:
        if isinstance(route, APIRoute):
            methods = ",".join(route.methods)
            path = route.path
            routes.append(f"{methods} {path}")  # one line per route

    return {"available_routes": routes}