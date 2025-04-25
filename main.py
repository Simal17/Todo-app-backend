from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api.schema import schema
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from database import engine

from dotenv import load_dotenv # type: ignore
load_dotenv()


Base.metadata.create_all(bind=engine)

graphql_router = GraphQLRouter(schema, path="/", graphql_ide="apollo-sandbox")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_router)
