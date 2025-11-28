import pytest
from unittest.mock import Mock
from uuid import UUID
from domain.entities.users import User
from application.use_cases.create_user_usecase import CreateUserUseCase
from domain.entities.passwords import Password
@pytest.fixture
def mock_user_repository():
    return Mock()

@pytest.fixture
def mock_password_hasher():
    return Mock()

def test_create_user_usecase_success(mock_user_repository, mock_password_hasher):
    # Arrange
    use_case = CreateUserUseCase(
        user_repository=mock_user_repository,
        password_hasher=mock_password_hasher
    )
    
    username = "testuser"
    email = "testuser@example.com"
    plain_text_password = "StrongP@ssw0rd!"
    hashed_password = "Hashedpassword@123"
    mock_password_hasher.hash.return_value = hashed_password
    created_user = User(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        username=username,
        email=email,
        _password=hashed_password
    )
    mock_user_repository.create.return_value = created_user     
    # Act
    result = use_case.execute(username, email, plain_text_password)
    # Assert
    mock_password_hasher.hash.assert_called_once_with(plain_text_password)
    mock_user_repository.create.assert_called_once()
    assert result == created_user
    assert result.username == username
    assert result.email == email

    assert result._password == hashed_password