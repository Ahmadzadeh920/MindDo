from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

class TaskStatus(str, Enum):

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"     
    FAILED = "failed"   
    ON_HOLD = "on_hold"


@dataclass
class Task:
    title: str
    id: UUID = field(default_factory=uuid4)
    user_id: UUID | None = None
    description: str = ""
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    
    # ------------------------------
    #   Initialization Validation
    # ------------------------------
    def __post_init__(self):
        if not isinstance(self.status, TaskStatus):
            raise ValueError(f"Invalid status: {self.status}")

    def update_status(self, new_status: TaskStatus):
        if not isinstance(new_status, TaskStatus):
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status
        self.updated_at = datetime.utcnow()

    def update_title(self, new_title: str):
        if not isinstance(new_title, str):
            raise ValueError("Invalid title type provided.")
        self.title = new_title
        self.updated_at = datetime.utcnow()

    def update_description(self, new_description: str):
        if not isinstance(new_description, str):
            raise ValueError("Invalid description type provided.")
        self.description = new_description
        self.updated_at = datetime.utcnow()

    def mark_as_completed(self):
        self.update_status(TaskStatus.COMPLETED)
        self.updated_at = datetime.utcnow()

    def mark_as_cancelled(self):
        self.update_status(TaskStatus.CANCELLED)
        self.updated_at = datetime.utcnow()

    def mark_as_failed(self):
        self.update_status(TaskStatus.FAILED)
        self.updated_at = datetime.utcnow()

    def mark_as_on_hold(self):
        self.update_status(TaskStatus.ON_HOLD)
        self.updated_at = datetime.utcnow()
    
    def mark_as_in_progress(self):
        self.update_status(TaskStatus.IN_PROGRESS)
        self.updated_at = datetime.utcnow()
    
    def mark_as_pending(self):
        self.update_status(TaskStatus.PENDING)
        self.updated_at = datetime.utcnow()

    

    