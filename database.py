from fastapi import Depends,FastAPI,HTTPException,Query
from sqlmodel import create_engine,Session,Field,SQLModel,select
from typing import Annotated


class Skill(SQLModel,table=True):
    id:int | None=Field(default=None,primary_key=True)

    name:str=Field(index=True)


database_url="sqlite:///skills.db"

engine=create_engine(database_url)

def create_db():
    SQLModel.metadata.create_all(engine)


