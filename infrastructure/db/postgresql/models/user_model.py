from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from infrastructure.db.sqlalchemy_engine import engine, Base
from infrastructure.db.postgresql.models.task_model import TaskModel
import uuid

class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to tasks
    tasks = relationship("TaskModel",back_populates="user",cascade="all, delete-orphan")
