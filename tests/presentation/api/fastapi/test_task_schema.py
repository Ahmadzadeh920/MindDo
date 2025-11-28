import pytest
from uuid import uuid4, UUID

from presentation.api.fastapi.schema.task_schema import (
    TaskCreateSchema,
    TaskUpdateSchema,
)
from domain.entities.tasks import Task, TaskStatus


class TestTaskSchemas:
    data = {
        "title": "Finish report",
        "description": "Write the annual report",
        "status": TaskStatus.IN_PROGRESS,
        "user_id": str(uuid4())
    }

    def test_task_create_schema_to_entity(self):
        schema = TaskCreateSchema(**self.data)
        task_entity = schema.to_entity()

        assert isinstance(task_entity, Task)
        assert task_entity.title == self.data["title"]
        assert task_entity.description == self.data["description"]
        assert task_entity.status == self.data["status"]
        assert str(task_entity.user_id) == str(self.data["user_id"])


    def test_task_update_schema_apply_updates(self):
        original_task = Task(
            title="Old Title",
            description="Old Description",
            status=TaskStatus.PENDING,
            user_id=uuid4()
        )

        update_data = {
            "title": "New Title",
            "description": "New Description",
            "status": TaskStatus.COMPLETED
        }
        schema = TaskUpdateSchema(**update_data)
        
        updated_task = schema.apply_updates(original_task)

        assert updated_task.title == update_data["title"]
        assert updated_task.description == update_data["description"]
        assert updated_task.status == update_data["status"]
