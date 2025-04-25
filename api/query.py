import strawberry
from .types.task import Task
from database import SessionLocal
from models import Task as TaskModel

@strawberry.type
class Query:
    @strawberry.field(description="Returns all tasks")
    def tasks(self) -> list[Task]:
        db = SessionLocal()
        task_models = db.query(TaskModel).all()
        db.close()
        return [
            Task(
                id=strawberry.ID(t.id),
                name=t.name,
                category=t.category,
                description=t.description,
                isFinished=t.isFinished,
                createdDate=t.createdDate,
                dueDate=t.dueDate,
                priority=t.priority
            )
            for t in task_models
        ]
