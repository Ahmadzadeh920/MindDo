from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from uuid import UUID
from domain.entities.passwords import Password, PasswordPolicyError
from domain.entities.users import User


class UserCreateSchema(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    password: str

    @validator("password")
    def validate_password(cls, v):
        try:
            Password(v)
        except PasswordPolicyError as e:
            raise ValueError(str(e))
        return v

    
    def to_entity(self) -> User:
        password_entity = Password(self.password)
        return User(
            username=self.username,
            email=self.email,
            _password=password_entity
        )

class UserUpdateSchema(BaseModel):
    username: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[EmailStr]
    password: Optional[str]

    @validator("password")
    def validate_password(cls, v):
        if v is not None:
            try:
                Password(v)
            except PasswordPolicyError as e:
                raise ValueError(str(e))
        return v
    def apply_updates(self, user: User) -> User:
        if self.username is not None:
            user.update_username(self.username)
        if self.email is not None:
            user.update_email(self.email)
        if self.password is not None:
            password_entity = Password(self.password)
            user.update_password(password_entity)
        return user 

class UserResponseSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    
    class Config:
        orm_mode = True