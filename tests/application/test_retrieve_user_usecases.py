import pytest
from unittest.mock import Mock
from application.use_cases.retrieve_user_usercases import RetrieveUserUseCase

class TestRetrieveUserUseCase:
    def setup_method(self):
        """
        Initialize mock repository and use case.
        """
        self.mock_user_repository = Mock()
        self.use_cases = RetrieveUserUseCase(user_repository=self.mock_user_repository)

        self.user_id = "abc-123"
        self.another_user_id = "abc-456"
        self.sample_user = {"id": self.user_id, "name": "Alice"}
        
    def retrieve_user_usercases_success(self):
        """
        Should return user when exists and permission is valid.
        """
        # Arrange
        self.mock_user_repository.get_by_id.return_value = self.sample_user
        #Act
        result = self.use_cases.execute(current_user_id=self.user_id, user_id=self.user_id)
        # Assert
        assert self.sample_user == result
        self.mock_user_repository.get_by_id.assert_called_once_with(self.user_id)


