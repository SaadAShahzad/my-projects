from fastapi import FastAPI
from pydantic import BaseModel

class Skill(BaseModel):
    name:str

s=["sql","java","python","ml","dl","cv"]    

app=FastAPI()


@app.get("/")
async def root():
    return {"message":"First API endpoint"}

@app.get("/student")
async def student():
    return {"name":"Saad","city":"rwp","semester":"6"}

@app.get("/skills")
async def skills():
    return s


@app.post("/add-skill")
async def add_skill(skill:Skill):
    s.append(skill.name)
    return s
