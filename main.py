from fastapi import FastAPI,Depends
from sqlmodel import Session,select
from database import Skill,engine,create_db

app=FastAPI()


@app.on_event("startup")
def on_startup():
    create_db()




@app.get("/")
async def root():
    return {"message":"First API endpoint"}



@app.get("/skills")
async def skills():
    with Session(engine) as db:
        results=db.exec(select(Skill)).all()
        return results
    

@app.post("/add-skill")
async def add_skill(skill: Skill):
    with Session(engine) as db:
        db.add(skill)
        db.commit()
        db.refresh(skill)
        return skill
