"""
Here are the methods required to store, retrieve, update, and delete tasks.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.tasks import Task
from uuid import UUID

class TaskRepository(ABC):
    """
    Abstract repository interface for Task persistence operations.

    This defines *what* operations are needed, not *how* they are implemented.
    Infrastructure layer (e.g., using PostgreSQL, SQLAlchemy) will provide
    concrete implementations of this interface.

    Example:
        class PostgresTaskRepository(ITaskRepository):
            def create(self, task: Task) -> Task:
                # Actual DB insert logic here
                pass
    """
    
    @abstractmethod
    def create(self, task: Task) -> Task:
        """Persist a new Task and return the created Task with ID."""
        pass

    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Optional[Task]:
        """Retrieve a Task by its ID. Returns None if not found."""
        pass

    @abstractmethod
    def list_all(self) -> List[Task]:
        """Return a list of all Tasks."""
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        """Update an existing Task and return the updated Task."""
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        """Delete a Task by its ID."""
        pass   


    @abstractmethod
    def list_by_user(self, user_id: UUID) -> List[Task]:
        """Return a list of Tasks for a specific user."""
        pass     