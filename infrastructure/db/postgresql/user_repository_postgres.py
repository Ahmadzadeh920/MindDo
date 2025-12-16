from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session
from zmq import has
from domain.entities.users import User
from domain.interfaces.user_repository import UserRepository
from infrastructure.db.postgresql.models.user_model import UserModel


class PostgresUserRepository(UserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, user: User) -> User:
        is_active = user.is_active if user.is_active is not None else True
        user_obj = UserModel(
            id=user.id,
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            is_active=is_active
        )
        self.db_session.add(user_obj)
        self.db_session.commit()
        self.db_session.refresh(user_obj)   
        return User(
            id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
            is_active=user_obj.is_active
        )
    
    def get_by_id(self, user_id: UUID) -> User | None:
        user_obj = self.db_session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_obj is None:
            return None
        return User(id=user_obj.id,
                    username=user_obj.username,
                    email=user_obj.email,
                    is_active=user_obj.is_active,
                    hashed_password=user_obj.hashed_password,)
    


    def get_by_email(self, email: str) -> User | None:
        user_obj = self.db_session.query(UserModel).filter(UserModel.email == email).first()
        if user_obj is None:
            return None
        return User(id=user_obj.id,
                    username=user_obj.username,
                    email=user_obj.email,
                    is_active=user_obj.is_active,
                    hashed_password=user_obj.hashed_password)
    

    def list_all(self) -> List[User]:
        user_objs = self.db_session.query(UserModel).all()
        return [User(id=user_obj.id,
                     username=user_obj.username,
                     email=user_obj.email,
                     is_active=user_obj.is_active) for user_obj in user_objs]
    
    def update(self, user: User) -> User:
        user_obj = self.db_session.query(UserModel).filter(UserModel.id == user.id).first()
        if user_obj is None:
            return None
        is_active = user.is_active if user.is_active is not None else True
        user_obj.username = user.username
        user_obj.email = user.email
        user_obj.hashed_password = user.password
        user_obj.is_active = is_active
        self.db_session.commit()
        self.db_session.refresh(user_obj)
        return User(id=user_obj.id,
                    username=user_obj.username,
                    email=user_obj.email,
                    is_active=user_obj.is_active,
                    hashed_password=user_obj.hashed_password,)   
    

    def delete(self, user_id: UUID) -> None:
        user_obj = self.db_session.query(UserModel).filter(UserModel.id == user_id).first()
        if not user_obj:
            raise ValueError("User not found")
        self.db_session.delete(user_obj)
        self.db_session.commit()

    def get_by_username_or_email(self, username_or_email: str) -> User | None:
        user_obj = (
            self.db_session.query(UserModel)
            .filter(
                (UserModel.username == username_or_email) |
                (UserModel.email == username_or_email)
            )
            .first()
        )

        if user_obj is None:
            return None

        return User(
            id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
            is_active=user_obj.is_active,
            hashed_password=user_obj.hashed_password,
            created_at=user_obj.created_at,
        )

