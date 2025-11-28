"""
Defines the abstract repository interface for user persistence operations.
"""

from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.users import User
from typing import Optional

class UserRepository(ABC):
    """
    Abstract repository interface for User persistence operations.

    This defines *what* operations are needed, not *how* they are implemented.
    Infrastructure layer (e.g., using PostgreSQL, SQLAlchemy) will provide
    concrete implementations of this interface.

    Example:
        class PostgresUserRepository(IUserRepository):
            def create(self, user: User) -> User:
                # Actual DB insert logic here
                pass
    """

    @abstractmethod
    def create(self, user: User) -> User:
        """Persist a new User and return the created User with ID."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        """Retrieve a User by its ID. Returns None if not found."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Retrieve a User by their email. Returns None if not found."""
        pass
    
    @abstractmethod
    def update(self, user: User) -> User:
        """Update an existing User and return the updated User."""
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        """Delete a User by its ID."""
        pass
        
    @abstractmethod
    def list_all(self) -> list[User]:   
        """Return a list of all Users."""
        pass