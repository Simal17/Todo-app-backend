import strawberry
from .query import Query
from .mutation import Mutation
from .types.task import Task

schema = strawberry.Schema(query=Query, types=[Task], mutation=Mutation)