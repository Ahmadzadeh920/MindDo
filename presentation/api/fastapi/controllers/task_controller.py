from fastapi import APIRouter, Depends, HTTPException, status
from domain.entities.tasks import TaskStatus
from infrastructure.db.dependencies import task_repository_dependency, get_current_user_id, user_repository_dependency
from application.use_cases.create_task_usecase import CreateTaskUseCase
from application.use_cases.retrieve_task_usercases import RetrieveTaskUseCase
from application.use_cases.update_task_usecase import UpdateTaskUseCase
from presentation.api.fastapi.schema.task_schema import TaskCreateSchema, TaskUpdateSchema, TaskResponseSchema




router= APIRouter(prefix="/tasks", tags=["tasks"])


# Create Task
@router.post("/", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(
    task_create: TaskCreateSchema,
    current_user_id: str = Depends(get_current_user_id),
    task_repository = Depends(task_repository_dependency),
    user_repository = Depends(user_repository_dependency)):
    use_case= CreateTaskUseCase(task_repository=task_repository, user_repository=user_repository)
    try:
        new_task = use_case.execute(task_data=task_create.model_dump(), current_user_id=current_user_id, user_id=task_create.user_id)
        return TaskResponseSchema.model_validate(new_task)
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except PermissionError as pe:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(pe))



# retrieve tasks for a user
@router.get("/tasks/{user_id}", response_model=list[TaskResponseSchema])
def retrieve_tasks_for_user(
    current_user_id: str = Depends(get_current_user_id),
    task_repository = Depends(task_repository_dependency),
    limit : int =0,
    off_set: int =0,
    user_repository = Depends(user_repository_dependency)):
    use_case= RetrieveTaskUseCase(user_repository=user_repository, task_repository=task_repository)
    try:
        tasks = use_case.execute(current_user_id=current_user_id, user_id=current_user_id)
        return [TaskResponseSchema.model_validate(task) for task in tasks]
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except PermissionError as pe:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(pe))  


# Update Task

@router.put("/{task_id}", response_model=TaskResponseSchema)
def update_task(
    task_id: str,
    task_update: TaskUpdateSchema,
    current_user_id: str = Depends(get_current_user_id),
    task_repository = Depends(task_repository_dependency),
    user_repository = Depends(user_repository_dependency)):
    use_case= UpdateTaskUseCase(task_repository=task_repository, user_repository=user_repository)
    try:
        updated_task= use_case.execute(updated=task_update.model_dump(exclude_unset=True), current_user_id=current_user_id, user_id=task_update.user_id, task_id=task_id)
        return TaskResponseSchema.model_validate(updated_task)
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except PermissionError as pe:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(pe))