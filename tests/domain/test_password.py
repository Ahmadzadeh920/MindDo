import pytest
from domain.entities.passwords import Password, PasswordPolicyError 
from domain.entities.users import User


# ----------------------------
#  Test valid password creation
# ----------------------------
def test_password_creation_valid():
    """Ensure a valid password is created correctly."""
    pwd = Password("StrongP@ssw0rd")
    assert pwd.value == "StrongP@ssw0rd"
    assert isinstance(pwd.value, str)

# ----------------------------
#  Test invalid password lengths
# ----------------------------
@pytest.mark.parametrize("invalid_password", [
    "Short1!",         # too short
    "aB1!",            # way too short
    "asdfgg@12",
    "Asdsdddk",
    "UPPERCASE1!",
])
def test_password_too_short(invalid_password):
    """Passwords IA NOT INVALID"""
    with pytest.raises(PasswordPolicyError):
        Password(invalid_password)