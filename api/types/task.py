import strawberry
from typing import Optional

@strawberry.type(
  description="A single task"
)
class Task:
  id: strawberry.ID = strawberry.field(description="The ID for the task.")
  name: str = strawberry.field(description="The name of the task")
  category: str = strawberry.field(description="The category of the task")
  description: Optional[str] = strawberry.field(description="The description of the task")
  isFinished: bool = strawberry.field(description="The status of the task")
  createdDate: str = strawberry.field(description="The created date of the task")
  dueDate: Optional[str] = strawberry.field(description="The due date of the task")
  priority: int = strawberry.field(description="The priority of the task")

@strawberry.input(description="Input fields for creating a new task")
class TaskInput:
  name: str = strawberry.field(description="The name of the task")
  category: str = strawberry.field(description="The category of the task")
  description: Optional[str] = strawberry.field(description="The description of the task")
  isFinished: bool = strawberry.field(description="The status of the task")
  createdDate: str = strawberry.field(description="The created date of the task")
  dueDate: Optional[str] = strawberry.field(description="The due date of the task")
  priority: int = strawberry.field(description="The priority of the task")

@strawberry.type(description="The response returned after attempting to create a task.")
class CreateTaskResponse:
    code: int = strawberry.field(description="HTTP-like status code representing the result.")
    success: bool = strawberry.field(description="Indicates whether the task was successfully created.")
    message: str = strawberry.field(description="A message about the mutation result.")
    task: Optional[Task] = strawberry.field(description="The task that was created, if successful.")
