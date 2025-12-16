from passlib.context import CryptContext

from domain.services.password_hasher import IPasswordHasher

# Define the hashing context (bcrypt is recommended)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHasherPasslib(IPasswordHasher):
    """Passlib-based implementation of password hashing."""
    def hash(self, plain_text: str) -> str:
        return pwd_context.hash(plain_text)

    
    def verify(self, plain_text: str, hashed: str) -> bool:
        return pwd_context.verify(plain_text, hashed)