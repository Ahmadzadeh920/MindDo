from uuid import UUID, uuid4
import pytest
from unittest.mock import Mock
from domain.entities.tasks import Task , TaskStatus
from application.use_cases.create_task_usecase import CreateTaskUseCase 

@pytest.fixture
def mock_task_repository():
    return Mock()

@pytest.fixture
def mock_user_repository():
    return Mock()


def test_create_task_success(mock_task_repository,mock_user_repository):
    usecases = CreateTaskUseCase(mock_task_repository, mock_user_repository)
    mock_user_repository.get_by_id.return_value= {"id": "user-123"}  # user exists
    task_data = {"title": "Finish documentation", "description": "Write API docs" ,"status":TaskStatus.PENDING}

    #Act
    task_obj= usecases.execute(user_id="user-123", task_data=task_data, current_user_id="user-123")
    
     # Assert
    assert isinstance(task_obj, Task)
    assert task_obj.user_id == "user-123"
    assert task_obj.title == "Finish documentation"
    assert isinstance(task_obj.status, TaskStatus)
