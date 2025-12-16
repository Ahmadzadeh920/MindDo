from pydantic import BaseModel, Field, field_validator

from typing import Optional 
from domain.entities.tasks import Task, TaskStatus


# ============================================
# Base Schema (Shared by Create, Update, Response)
# ============================================
class BaseTaskSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    status: Optional[TaskStatus]

    # Centralized validation
    @field_validator("status", mode="before")
    def validate_status(cls, v):
        if v is None:
            return None
        if not isinstance(v, TaskStatus):
            try:
                return TaskStatus(v)
            except ValueError:
                raise ValueError(f"Invalid status value: {v}")
        return v


class TaskCreateSchema(BaseTaskSchema):
    title: str = Field(..., min_length=1, max_length=100)
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    user_id: str

    

    def to_entity(self) -> Task:
        return Task(
            title=self.title,
            description=self.description,
            status=self.status,
            user_id=self.user_id
        )


class TaskUpdateSchema(BaseTaskSchema):
   
    def apply_updates(self, task:Task)-> Task:
        if self.title is not None:
            task.update_title(new_title=self.title)
        if self.description is not None:
            task.update_description(new_description=self.description)
        if self.status is not None:
            task.update_status(new_status=self.status)
        return task

class TaskResponseSchema(BaseTaskSchema):
    id: str
    title: str
    description: Optional[str]
    status: TaskStatus
    user_id: str

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True}