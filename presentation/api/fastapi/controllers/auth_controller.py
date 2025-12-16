from fastapi import APIRouter, Depends, HTTPException, status
from typing import Any
from infrastructure.auth import jwt_manager
from presentation.api.fastapi.schema.auth_shema import LoginSchema
from presentation.api.fastapi.schema.user_schema import UserCreateSchema, UserResponseSchema, UserUpdateSchema
import infrastructure.db.dependencies as deps 
from application.use_cases.login_user_usecase import LoginUseCase
from application.use_cases.create_user_usecase import CreateUserUseCase

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def register(
    payload: UserCreateSchema,
    usecase: deps.CreateUserUseCase = Depends(deps.get_create_user_usecase),
) -> Any:
    try:
        created_user = usecase.execute(
            username=payload.username,
            email=payload.email,
            plain_text_password=payload.password,
        )
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return created_user


@router.post("/login")
def login(
    payload: LoginSchema,
    usecase: deps.LoginUseCase = Depends(deps.get_login_usecase),
) -> dict:
    result = usecase.execute(username_or_email=payload.username_or_email, plain_password=payload.password)
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {
        "access_token": result["access_token"],
        "refresh_token": result.get("refresh_token"),
        "token_type": "bearer",
    }


@router.post("/test")
def test(
    payload: LoginSchema,
    passlib_hasher = Depends(deps.get_password_hasher),
) -> dict:
    result = passlib_hasher.verify(payload.password, "$2b$12$9JnkiHEIToiQu3FogvoHju8spowgjHDBCy8U8lrJh4UFFQF8PvYwO")
    return {"result": result}
