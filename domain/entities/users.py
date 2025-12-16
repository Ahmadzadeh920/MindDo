from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from domain.entities.passwords import Password

@dataclass
class User:
    username: str
    email: str
    hashed_password: str = field(default="")
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    is_active: bool = field(default=True)

    @property
    def password(self) -> Password:
        """
        Returns the plain password (for hashing in infrastructure layer).
        Domain layer never hashes directly.
        """
        return self.hashed_password

    def update_username(self, new_username: str):
        if not new_username.strip():
            raise ValueError("Invalid username type provided.")
        self.username = new_username
        self.updated_at = datetime.now()

    def update_email(self, new_email: str):
        if "@" not in new_email or not new_email.strip():
            raise ValueError("Invalid email address.")
        self.email = new_email
        self.updated_at = datetime.now()

    def update_password(self, new_hashed_password: str):
        if not new_hashed_password:
            raise ValueError("Invalid hashed password provided.")
        self.hashed_password = new_hashed_password
        self.updated_at = datetime.now()