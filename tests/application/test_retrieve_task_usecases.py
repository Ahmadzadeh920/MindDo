import pytest
from unittest.mock import Mock
from application.use_cases.retrieve_task_usercases import RetrieveTaskUseCase





class test_retrieve_tasks_success:
    def setup_method(self):
        """
        Initialize mock repositories and use case before each test.
        """
        self.mock_task_repository = Mock()
        self.mock_user_repository = Mock()
        self.usecases = RetrieveTaskUseCase(
            user_repository=self.mock_user_repository,
            task_repository=self.mock_task_repository
        )
        self.user_id = "user-123"
        self.current_user_id = "user-123"   
        self.sample_tasks = [
            {"id": "task-1", "title": "Task A"},
            {"id": "task-2", "title": "Task B"},
        ]

    def test_retrieve_tasks_success(self):
        self.mock_user_repository.get_by_id.return_value = {"id": self.user_id}  # User exists
        self.mock_task_repository.list_by_user.return_value = self.sample_tasks
        # Act
        tasks = self.usecases.execute(
            current_user_id=self.current_user_id,
            user_id=self.user_id
        )
        # Assert
        assert len(tasks) == len(self.sample_tasks)
        self.mock_user_repository.get_by_id.assert_called_once_with(self.user_id)
        self.mock_task_repository.list_by_user.assert_called_once_with(user_id=self.user_id)

