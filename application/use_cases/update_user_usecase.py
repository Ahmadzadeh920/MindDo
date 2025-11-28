
from domain.interfaces.user_repository import UserRepository
from domain.entities.users import User




class UpdateUserUseCase:
    """
    Use case for creating a new task associated with a user.

    This class encapsulates the business logic for task creation,
    ensuring that tasks are properly linked to users.
    """

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, updated:dict, current_user_id:str, user_id:str) -> 'User':
        """
        Update an existing user's information.

        :param current_user_id: ID of the user performing the update
        :param user_id: ID of the user to update
        :param updates: Dictionary containing fields to update
        :return: Updated User
        """
        # Verify that the user exists
        user_obj = self.user_repository.get_by_id(user_id)
        if not user_obj:
            raise ValueError("User not found")

        if str(user_id) != current_user_id:
            raise PermissionError("Cannot create task for another user")
        
        
        

        for key, value in updated.items():
            setattr(user_obj, key , value)


        updated_user= self.user_repository.update(user_obj)
        return updated_user


    
