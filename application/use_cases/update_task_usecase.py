from domain.interfaces.task_repository import TaskRepository
from domain.interfaces.user_repository import UserRepository
from domain.entities.tasks import TaskStatus, Task


class UpdateTaskUseCase:
    """
    Use case for creating a new task associated with a user.

    This class encapsulates the business logic for task creation,
    ensuring that tasks are properly linked to users.
    """

    def __init__(self, task_repository: TaskRepository, user_repository: UserRepository):
        self.task_repository = task_repository
        self.user_repository = user_repository

    def execute(self, updated:dict, current_user_id:str, user_id:str, task_id) -> 'Task':
        # Verify that the user exists
        user_obj = self.user_repository.get_by_id(user_id)
        if not user_obj:
            raise ValueError("User not found")

        if str(user_id) != current_user_id:
            raise PermissionError("Cannot create task for another user")
        
        if "status" in updated:
            if not isinstance(updated["status"], TaskStatus):
                raise ValueError(f"Status must be of type TaskStatus, got {type(updates['status'])}")
        
        task = self.task_repository.get_by_id(task_id)

        if str(task.user_id) != str(user_id):
            raise PermissionError("You are not allowed to update this task")

        for key, value in updated.items():
            setattr(task, key , value)


        updated_task = self.task_repository.update(task)
        return updated_task


    
