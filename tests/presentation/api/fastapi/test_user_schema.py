import pytest
from uuid import uuid4, UUID


from pydantic import ValidationError

from presentation.api.fastapi.schema.user_schema import (
    UserCreateSchema,
    UserUpdateSchema,
    UserResponseSchema
)

from domain.entities.users import User
from domain.entities.passwords import Password, PasswordPolicyError


class TastUserCreateSchema:
    def test_create_schema_valid(self):
        data ={
            "username":"test_schema",
            "email": "test@schema.com",
            "password": "StrongPass1!"

        }

        user_obj = UserCreateSchema(**data).to_entity()

        assert isinstance(user_obj, User)
        assert user_obj.username == "test_schema"
        assert isinstance(entity._password, Password)

    def test_password_invalid(self):
        data ={
            "username":"test_schema",
            "email": "test@schema.com",
            "password": "weak!"

        }

        with pytest.ValidationError: UserCreateSchema(**data)

class TestUserUpdateSchema:
    def test_update_schema_valid(self):
        updated_user ={
            "username":"updated_user",
            "email": "updated@user.com",
            "password": "NewStrongPass1!"
        }
        old_user={
            "username":"old_name",
            "email":"old@mail.com",
            "_password": Password("OldPass1!")
        }

        user_entity = User(**old_user)
        update_schema = UserUpdateSchema(**updated_user)
        updated_entity = update_schema.apply_updates(user_entity)

        assert updated_entity.username == "updated_user"
        assert updated_entity.email == "updated@user.com"   
    def test_update_schema_invalid_password(self):
        updated_user ={
            "password": "weak"
        }
        old_user = {
            "username":"old_name",
            "email":"test@schema.com",
            "_password": Password("OldPass1!")  }
        user_entity = User(**old_user)
        with pytest.raises(ValidationError):
            update_schema = UserUpdateSchema(**updated_user)
            update_schema.apply_updates(user_entity)        


class TestUserResponseSchema:
    def test_response_schema(self):
        user = User(
            username="john",
            email="john@example.com",
            _password=Password("StrongPass1!")
        )

        schema = UserResponseSchema(
            id=user.id,
            username=user.username,
            email=user.email,
        )

        assert schema.id == user.id
        assert isinstance(schema.id, UUID)
        assert schema.username == "john"
        assert schema.email == "john@example.com"