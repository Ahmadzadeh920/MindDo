from uuid import uuid4, UUID
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.task_repository import TaskRepository
from domain.entities.tasks import Task, TaskStatus
class CreateTaskUseCase:
    """
    Use case for creating a new task associated with a user.

    This class encapsulates the business logic for task creation,
    ensuring that tasks are properly linked to users.
    """

    def __init__(self, task_repository: TaskRepository, user_repository: UserRepository):
        self.task_repository = task_repository
        self.user_repository = user_repository

    def execute(self, task_data:dict, current_user_id:str, user_id:str) -> 'Task':
        # Verify that the user exists
        user_obj = self.user_repository.get_by_id(user_id)
        if not user_obj:
            raise ValueError("User not found")

        if str(user_id) != current_user_id:
            raise PermissionError("Cannot create task for another user")
        
        new_task = Task(
            id=str(uuid4()),
            title=task_data.get("title"),
            description=task_data.get("description",""),
            user_id=user_id,
            status=task_data.get("status", TaskStatus.PENDING)
        )
        self.task_repository.create(new_task)
        return new_task