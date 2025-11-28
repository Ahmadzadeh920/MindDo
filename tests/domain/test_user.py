import pytest
from datetime import datetime, timedelta
from uuid import UUID
from domain.entities.users import User
from domain.entities.passwords import Password, PasswordPolicyError 


# ---------------------------------------------------------------------
#  Fixture: a reusable user instance
# ---------------------------------------------------------------------
@pytest.fixture
def sample_user() -> User:
    return User(
        username="testuser",
        _password=Password("SecureP@ssw0rd!"),
        email="testuser@example.com"
    )

# ---------------------------------------------------------------------
#  Test Cases for User Entity
# ---------------------------------------------------------------------
def test_user_creation(sample_user: User):
    assert isinstance(sample_user.id, UUID)
    assert sample_user.username == "testuser"
    assert sample_user.password == "SecureP@ssw0rd!"
    assert isinstance(sample_user.created_at, datetime)
    assert isinstance(sample_user.updated_at, datetime)
    assert sample_user.created_at <= sample_user.updated_at
    
# ---------------------------------------------------------------------
#  Username updates
# ---------------------------------------------------------------------

def test_update_username(sample_user: User):
    old_updated_at = sample_user.updated_at
    sample_user.update_username("newusername")
    assert sample_user.username == "newusername"
    assert sample_user.updated_at > old_updated_at

def test_update_username_invalid(sample_user: User):
    with pytest.raises(ValueError):
        sample_user.update_username("   ")  # Invalid username

# ----------------------------
#  Tests for email updates
# ----------------------------

def test_update_email(sample_user: User):
    old_updated_at = sample_user.updated_at
    sample_user.update_email("admin@gmail.com")
    assert sample_user.email == "admin@gmail.com"
    assert sample_user.updated_at > old_updated_at

# ----------------------------
#  Tests for password updates
# ----------------------------

def test_password_update(sample_user: User):
    old_updated_at = sample_user.updated_at
    new_password = Password("NewS3cur3P@ss!")
    sample_user.update_password(new_password)
    assert sample_user.password == "NewS3cur3P@ss!"
    assert sample_user.updated_at > old_updated_at


def test_update_password_invalid_type(sample_user: User):
    with pytest.raises(ValueError):
        sample_user.update_password("NotAPasswordInstance")  # Invalid type

# ----------------------------
#  Edge: Password policy violations
# ----------------------------
@pytest.mark.parametrize("invalid_password", [
    "short1!",         # too short
    "nocaps1!",        # no uppercase
    "NOLOWERCASE1!",   # no lowercase
    "NoSpecial123",    # no special char
    "NoNumber!"        # no number
])
def test_password_policy_violations(invalid_password):
    """Ensure Password raises PasswordPolicyError for invalid passwords."""
    with pytest.raises(PasswordPolicyError):
        Password(invalid_password)