from uuid import UUID, uuid4
from domain.entities.users import User
from domain.entities.passwords import Password
from domain.interfaces.user_repository import UserRepository    
from domain.services.password_hasher import IPasswordHasher
from domain.services.normalizers import normalize_username


class CreateUserUseCase:
    """
    Use case for creating a new user.

    This class encapsulates the business logic for user creation,
    including password hashing and user data validation.
    """

    def __init__(self, user_repository:UserRepository, password_hasher: IPasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher


    def execute(self,   username: str, email: str, plain_text_password: str) -> User:
        hashed_password = self.password_hasher.hash(plain_text_password)
       
        normalized_username = normalize_username(username)
        new_user = User(
            id=uuid4(),  # <--- GENERATE A NEW, UNIQUE UUID HERE
            username=normalized_username,
            email=email,
            hashed_password=hashed_password
        )

        created_user = self.user_repository.create(new_user)
        return created_user

        