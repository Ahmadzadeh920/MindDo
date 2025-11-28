from uuid import UUID
from domain.entities.users import User
from domain.interfaces.user_repository import UserRepository    


class RetrieveUserUseCase:
    """
    Use case for retrieving  user.

   
    """

    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository
       

    def execute(self, current_user_id: str , user_id: str) -> User:
        """
        Retrieve a user by ID.

        - The user must exist.
        - Users can only retrieve their own info (permission check).
        """
        user_obj = self.user_repository.get_by_id(user_id)
        if not user_obj:
            raise ValueError("User not found")

        if str(user_id) != str(current_user_id):
            raise PermissionError("You are not allowed to view another user's info")

        return user_obj


        
        
       
        