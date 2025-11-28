from pydantic import BaseModel, Field, validator

from typing import Optional 
from domain.entities.tasks import Task, TaskStatus

class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] 
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    user_id: str

    @validator("status")
    def validate_status(cls, v, pre = True, always = True):
        if v is None:
            return TaskStatus.PENDING
        if not isinstance(v, TaskStatus):
            try:
                v = TaskStatus(v)
            except ValueError:
                raise ValueError(f"Invalid status value: {v}")
        return v

    def to_entity(self) -> Task:
        return Task(
            title=self.title,
            description=self.description,
            status=self.status,
            user_id=self.user_id
        )


class TaskUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    status: Optional[TaskStatus]

    @validator("status")
    def validate_status(cls, v):
        if v is not None and not isinstance(v, TaskStatus):
            try:
                v = TaskStatus(v)
            except ValueError:
                raise ValueError(f"Invalid status value: {v}")
        return v

    def apply_updates(self, task:Task)-> Task:
        if self.title is not None:
            task.update_title(new_title=self.title)
        if self.description is not None:
            task.update_description(new_description=self.description)
        if self.status is not None:
            task.update_status(new_status=self.status)
        return task

class TaskResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: TaskStatus
    user_id: str

    class Config:
        orm_mode = True