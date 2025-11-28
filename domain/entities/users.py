from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from domain.entities.passwords import Password

@dataclass
class User:
    username: str
    _password: Password
    email: str
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


    @property
    def password(self) -> Password:
        """
        Returns the plain password (for hashing in infrastructure layer).
        Domain layer never hashes directly.
        """
        return self._password.value

    def update_username(self, new_username: str):
        if not new_username.strip():
            raise ValueError("Invalid username type provided.")
        self.username = new_username
        self.updated_at = datetime.utcnow()

    def update_email(self, new_email: str):
        if "@" not in new_email or not new_email.strip():
            raise ValueError("Invalid email address.")
        self.email = new_email
        self.updated_at = datetime.utcnow()

    def update_password(self, new_password: Password):
        if not isinstance(new_password, Password):
            raise ValueError("Invalid password type provided.")
        self._password = new_password
        self.updated_at = datetime.utcnow()