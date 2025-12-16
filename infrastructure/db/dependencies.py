import uuid

from sqlalchemy import Uuid
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Generator
from uuid import UUID
from fastapi.security import OAuth2PasswordBearer

from infrastructure.db.sqlalchemy_engine import get_db_session
from infrastructure.db.postgresql.task_repository_postgres import PostgresTaskRepository
from infrastructure.db.postgresql.user_repository_postgres import PostgresUserRepository
from infrastructure.auth.password_hasher_passlib import PasswordHasherPasslib
from infrastructure.auth.jwt_manager import JWTManager
from domain.interfaces.task_repository import TaskRepository
from domain.interfaces.user_repository import UserRepository
from application.use_cases.create_user_usecase import CreateUserUseCase
from application.use_cases.login_user_usecase import LoginUseCase



def get_password_hasher():
    return PasswordHasherPasslib()

# clients will obtain a token by sending credentials to POST /auth/login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def task_repository_dependency(db: Session = Depends(get_db_session)) -> TaskRepository:
    """
    Dependency that provides an instance of TaskRepository.
    """
    return PostgresTaskRepository(db_session=db)
   

def user_repository_dependency(db:Session = Depends(get_db_session)) -> UserRepository:
    return PostgresUserRepository(db_session=db)


def get_jwt_manager():
    return JWTManager()

def get_current_user_id(
        token: str =Depends(oauth2_scheme),
        jwt_manager: JWTManager =Depends(get_jwt_manager),
        user_repo =Depends(user_repository_dependency)
):
    try:
        payload = jwt_manager.verify_token(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth token")
    jti = payload.get("jti")

    user_id = payload.get("subject")
    user_obj = user_repo.get_by_id(user_id)

    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user_obj
    

def get_create_user_usecase(
    user_repo = Depends(user_repository_dependency),
    password_hasher =Depends(get_password_hasher),  # module-level instance is fine
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository=user_repo, password_hasher=password_hasher)
    

def get_login_usecase(
    user_repo = Depends(user_repository_dependency),
    password_hasher =Depends(get_password_hasher),
    jwt_manager = Depends(get_jwt_manager),
) -> LoginUseCase:
    return LoginUseCase(user_repo=user_repo, jwt_provider=jwt_manager, password_hasher=password_hasher)

    




