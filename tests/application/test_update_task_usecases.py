import pytest
from unittest.mock import Mock
from domain.entities.tasks import Task, TaskStatus
from application.use_cases.update_task_usecase import UpdateTaskUseCase

class TestUpdateTaskUseCase:
    """
    Tests for UpdateTaskUseCase using mocks for task and user repositories.
    """
    def setup_method(self):
        # Initialize mocks
        self.mock_user_repo = Mock()
        self.mock_task_repo = Mock()
        self.use_case = UpdateTaskUseCase(
            task_repository=self.mock_task_repo,
            user_repository=self.mock_user_repo
        )

        # Sample data
        self.user_id = "user-123"
        self.other_user_id = "user-456"
        self.task_id = "task-123"
        self.sample_user = {"id": self.user_id, "name": "Alice"}
        self.sample_task = Task(
            id=self.task_id,
            user_id=self.user_id,
            title="Old Task",
            description="Old description",
            status=TaskStatus.PENDING
        )

    def test_update_task_success(self):
        # Arrange
        self.mock_user_repo.get_by_id.return_value = self.sample_user
        self.mock_task_repo.get_by_id.return_value = self.sample_task
        self.mock_task_repo.update.return_value = self.sample_task
        updates = {"title": "New Title", "status": TaskStatus.COMPLETED}

        result = self.use_case.execute(updated=updates,
                            current_user_id=self.user_id,
                            user_id=self.user_id,
                            task_id=self.task_id)

        # Assert
        assert result == self.sample_task
        assert self.sample_task.title == "New Title"
        assert self.sample_task.status == TaskStatus.COMPLETED
        self.mock_user_repo.get_by_id.assert_called_once_with(self.user_id)
        self.mock_task_repo.get_by_id.assert_called_once_with(self.task_id)
        self.mock_task_repo.update.assert_called_once_with(self.sample_task)