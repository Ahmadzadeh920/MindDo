
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.task_repository import TaskRepository

class RetrieveTaskUseCase:
    """
    Use case for retrieving  tasks associated with a user.
    """

    def __init__(self,user_repository: UserRepository, task_repository: TaskRepository):
        
        self.user_repository = user_repository
        self.task_repository = task_repository 

    def execute(self, current_user_id:str, user_id:str) -> 'Task':
        # Verify that the user exists
        user_obj = self.user_repository.get_by_id(user_id)
        if not user_obj:
            raise ValueError("User not found")

        if str(user_id) != str(current_user_id):
            raise PermissionError("Cannot create task for another user")
        
        
        tasks = self.task_repository.list_by_user(user_id=user_id)
        return tasks