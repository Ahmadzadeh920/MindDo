from abc import ABC, abstractmethod
from typing import Dict, Any
class IJWTProvider(ABC):
    """Interface for JWT operations used by use-cases."""

    @abstractmethod
    def create_access_token(self, subject: str) -> str:
        pass

    @abstractmethod
    def create_refresh_token(self, subject: str) -> str:
        pass

    @abstractmethod
    def verify_token(self, token: str) -> Dict[str, Any]:
        pass