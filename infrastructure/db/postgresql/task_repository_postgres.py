from sqlalchemy.orm import Session
from uuid import UUID
from domain.entities.tasks import Task
from domain.interfaces.task_repository import TaskRepository


class PostgresTaskRepository(TaskRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, task: Task) -> Task:
        self.db_session.add(task)
        self.db_session.commit()
        self.db_session.refresh(task)
        return task
    
    def get_by_id(self, task_id: UUID) -> Task:
        return self.db_session.query(Task).filter(Task.id == task_id).first()
    

    def list_all(self) -> list[Task]:
        return self.db_session.query(Task).all()
    
    def update(self, task: Task) -> Task:
        
        self.db_session.commit()
        self.db_session.refresh(task)
        return task
    

    def delete(self, task_id: UUID) -> None:
        task = self.get_by_id(task_id)
        if task:
            self.db_session.delete(task)
            self.db_session.commit()   


    def list_by_user(self, user_id: UUID) -> list[Task]:
        return self.db_session.query(Task).filter(Task.user_id == user_id).all()     