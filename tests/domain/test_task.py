import pytest
from domain.entities.tasks import Task, TaskStatus
from uuid import UUID
from datetime import datetime, timedelta

def test_create_task_with_valid_data():
    task = Task(title="Test Task", description="This is a test task.")
    assert isinstance(task.id, UUID)
    assert task.title == "Test Task"
    assert task.description == "This is a test task."
    assert task.status == TaskStatus.PENDING
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_invalid_status_raises_value_error():
    with pytest.raises(ValueError):
        Task(title="Invalid task", status="unknown_status")  # invalid enum


def test_update_title_success():
    task = Task(title="Initial Title")
    task.update_title("Updated Title")
    task.update_at = datetime.utcnow() + timedelta(seconds=1)  # simulate time passage
    assert task.title == "Updated Title"
    assert task.updated_at > task.created_at


def test_update_title_invalid_type():
    task = Task(title="Initial Title")
    with pytest.raises(ValueError):
        task.update_title(123)  # invalid type

def test_update_description_success():
    task = Task(title="Task 1", description="Initial description")
    old_updated_at = task.updated_at
    task.update_description("Updated description")
    assert task.description == "Updated description"
    assert task.updated_at > old_updated_at


def test_update_description_invalid_type():
    task = Task(title="Desc test")
    with pytest.raises(ValueError):
        task.update_description(12345)  # invalid type

# ------------------------------------------------------------
#  Mark Methods (Status Transitions)
# ------------------------------------------------------------
@pytest.mark.parametrize("method, expected_status", [
    ("mark_as_completed", TaskStatus.COMPLETED),
    ("mark_as_cancelled", TaskStatus.CANCELLED),
    ("mark_as_failed", TaskStatus.FAILED),
    ("mark_as_on_hold", TaskStatus.ON_HOLD),
    ("mark_as_in_progress", TaskStatus.IN_PROGRESS),
    ("mark_as_pending", TaskStatus.PENDING),
])

def test_mark_methods(method, expected_status):
    task = Task(title="Status Transition Test")
    old_updated_at = task.updated_at
    getattr(task, method)()  # Call the method dynamically
    assert task.status == expected_status
    assert task.updated_at > old_updated_at



