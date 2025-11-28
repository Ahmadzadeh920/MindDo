from abc import ABC, abstractmethod

class IPasswordHasher(ABC):
    """Interface for password hashing implementations."""
    """IPasswordHasher is an abstract interface — actual hashing (bcrypt, Argon2, etc.) will be implemented in the infrastructure layer."""
    
    @abstractmethod
    def hash(self, plain_text: str) -> str:
        pass

    @abstractmethod
    def verify(self, plain_text: str, hashed: str) -> bool:
        pass