import pytest
from unittest.mock import Mock
from domain.entities.users import User
from domain.entities.passwords import Password
from application.use_cases.update_user_usecase import UpdateUserUseCase


class TestUpdateUserUseCase:
    """
    Tests for UpdateUserUseCase using mock user repository.
    """

    def setup_method(self):
        # Initialize mock repository and use case
        self.mock_user_repo = Mock()
        self.use_case = UpdateUserUseCase(user_repository=self.mock_user_repo)

        # Sample data
        self.user_id = "user-123"
        self.other_user_id = "user-456"
        self.sample_user = User(id=self.user_id, username="Alice", email="alice@example.com", _password=Password("hashedPwd@12222"))

    def test_update_user_success(self):
        # Arrange
        self.mock_user_repo.get_by_id.return_value = self.sample_user
        self.mock_user_repo.update.return_value = self.sample_user
        updates = {"name": "Alice Updated", "email": "alice.new@example.com"}

        # Act
        result = self.use_case.execute(
            updated=updates,
            current_user_id=self.user_id,
            user_id=self.user_id
        )

        # Assert
        assert result == self.sample_user
        assert self.sample_user.name == "Alice Updated"
        assert self.sample_user.email == "alice.new@example.com"
        self.mock_user_repo.get_by_id.assert_called_once_with(self.user_id)
        self.mock_user_repo.update.assert_called_once_with(self.sample_user)

    def test_update_user_not_found(self):
        # Arrange
        self.mock_user_repo.get_by_id.return_value = None
        updates = {"name": "New Name"}

        # Act + Assert
        with pytest.raises(ValueError, match="User not found"):
            self.use_case.execute(
                updated=updates,
                current_user_id=self.user_id,
                user_id=self.user_id
            )

    def test_update_user_permission_denied(self):
        # Arrange
        self.mock_user_repo.get_by_id.return_value = self.sample_user
        updates = {"name": "Alice Updated"}

        # Act + Assert
        with pytest.raises(PermissionError, match="Cannot create task for another user"):
            self.use_case.execute(
                updated=updates,
                current_user_id=self.other_user_id,
                user_id=self.user_id
            )
