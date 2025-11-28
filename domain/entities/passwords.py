from abc import ABC, abstractmethod
import re 

class PasswordPolicyError(ValueError):
    """Custom exception for invalid passwords."""
    pass


class Password:
  
    """
    Password entity handles validation rules — e.g., minimum length, complexity.
    """
    Min_Length = 8
    
    def __init__(self, plain_text: str):
        self._validate(plain_text)
        self._value = plain_text
    
    
    @property
    def value(self) -> str:
        """Returns the plain text password value."""
        return self._value

    def _validate(self, plain_text: str):
        if len(plain_text) < self.Min_Length:
            raise PasswordPolicyError(f"Password must be at least {self.Min_Length} characters long.")
        if not re.search(r"[A-Z]", plain_text):
            raise PasswordPolicyError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", plain_text):
            raise PasswordPolicyError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", plain_text):
            raise PasswordPolicyError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", plain_text):
            raise PasswordPolicyError("Password must contain at least one special character.")



    

