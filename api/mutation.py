from .types.task import Task, TaskInput, CreateTaskResponse
from models import Task as TaskModel
from database import SessionLocal
import strawberry
from typing import Optional, List
from openai import OpenAI # type: ignore
import os


@strawberry.type
class Mutation:

    @strawberry.mutation(description="Create a new task.")
    def create_task(self, input: TaskInput) -> CreateTaskResponse:
        try:
            db = SessionLocal()
            db_task = TaskModel(**input.__dict__)
            db.add(db_task)
            db.commit()
            db.refresh(db_task)
            db.close()

            return CreateTaskResponse(
                code=200,
                success=True,
                message="Task created successfully.",
                task=Task(
                    id=strawberry.ID(db_task.id),
                    name=db_task.name,
                    category=db_task.category,
                    description=db_task.description,
                    isFinished=db_task.isFinished,
                    createdDate=db_task.createdDate,
                    dueDate=db_task.dueDate,
                    priority=db_task.priority
                )
            )
        except Exception as e:
            return CreateTaskResponse(
                code=500,
                success=False,
                message=f"Error creating task: {str(e)}",
                task=None
            )

    @strawberry.mutation(description="Update a task by ID.")
    def update_task(self, id: strawberry.ID, input: TaskInput) -> CreateTaskResponse:
        try:
            db = SessionLocal()
            db_task = db.query(TaskModel).filter(TaskModel.id == id).first()

            if not db_task:
                return CreateTaskResponse(code=404, success=False, message="Task not found", task=None)

            for key, value in input.__dict__.items():
                setattr(db_task, key, value)

            db.commit()
            db.refresh(db_task)
            db.close()

            return CreateTaskResponse(
                code=200,
                success=True,
                message="Task updated successfully.",
                task=Task(
                    id=strawberry.ID(db_task.id),
                    name=db_task.name,
                    category=db_task.category,
                    description=db_task.description,
                    isFinished=db_task.isFinished,
                    createdDate=db_task.createdDate,
                    dueDate=db_task.dueDate,
                    priority=db_task.priority
                )
            )
        except Exception as e:
            return CreateTaskResponse(code=500, success=False, message=f"Error updating task: {str(e)}", task=None)

    @strawberry.mutation(description="Delete a task by ID.")
    def delete_task(self, id: strawberry.ID) -> CreateTaskResponse:
        try:
            db = SessionLocal()
            db_task = db.query(TaskModel).filter(TaskModel.id == id).first()

            if not db_task:
                return CreateTaskResponse(code=404, success=False, message="Task not found", task=None)

            db.delete(db_task)
            db.commit()
            db.close()

            return CreateTaskResponse(
                code=200,
                success=True,
                message="Task deleted successfully",
                task=None
            )
        except Exception as e:
            return CreateTaskResponse(code=500, success=False, message=f"Error deleting task: {str(e)}", task=None)

    @strawberry.mutation(description="Generate a new todo based on existing tasks.")
    def generate_task(self, existing: List[str]) -> str:
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            prompt = (
                "You are an intelligent assistant that helps users manage their todo tasks.\n\n"
                "Given the following todo tasks:\n"
                + "\n".join(f"- {task}" for task in existing)
                + "\n\nSuggest one **relevant and realistic** new task. Constraints:\n"
                "- Output must be in dictionary format (key: value), one per line.\n"
                "- Use these exact keys: name, category, description, priority, dueDate.\n"
                "- Category must be one of: Work, School, Personal, Others.\n"
                "- Priority must be 1 (low), 2 (medium), or 3 (high).\n"
                "- dueDate must be a future date in format YYYY-MM-DD.\n"
                "- Make sure dueDate is no later than the latest dueDate in the input.\n"
                "- Favor high priority + near due dates for task relevance.\n\n"
                "Example output:\n"
                "name: Finish budget proposal\n"
                "category: Work\n"
                "description: Compile financials and finalize the document\n"
                "priority: 3\n"
                "dueDate: 2025-04-24\n\n"
                "Now generate one such task:"
            )

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )

            suggestion = response.choices[0].message.content.strip()
            return suggestion

        except Exception as e:
            return f"[Error] Failed to generate task: {str(e)}"
