# presentation/api/fastapi/schema/auth_schema.py
from pydantic import BaseModel, Field
from typing import Optional

class LoginSchema(BaseModel):
    username_or_email: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)

