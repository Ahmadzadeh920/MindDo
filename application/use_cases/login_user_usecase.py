from domain.interfaces.user_repository import UserRepository
from domain.services.password_hasher import IPasswordHasher
from domain.interfaces.jwt_provider import IJWTProvider

class LoginUseCase:
    def __init__(self, user_repo: UserRepository , jwt_provider: IJWTProvider, password_hasher: IPasswordHasher):
        self.user_repo = user_repo
        self.jwt_provider = jwt_provider
        self.password_hasher = password_hasher

    def execute(self, username_or_email: str, plain_password : str):
        user = self.user_repo.get_by_username_or_email(username_or_email)
        '''if not user or not self.password_hasher.verify(plain_password, user.hashed_password):
            return None'''
        if not user:
            return None
        if not self.password_hasher.verify(plain_password, user.hashed_password):   
            return {"error": "not verify password"}
        access_token = self.jwt_provider.create_access_token(str(user.id))
        refresh_token = self.jwt_provider.create_refresh_token(str(user.id))
        return {"access_token": access_token, "refresh_token": refresh_token}