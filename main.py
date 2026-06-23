from fastapi import FastAPI,Depends,HTTPException
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

 
@app.get("/skills/{id}")
async def skill_id(id:int):
    with Session(engine) as db:
        s=db.exec(select(Skill).where(Skill.id==id)).first()
        if s==None:
            raise HTTPException(status_code=404,detail="id not found")
        return s

@app.post("/add-skill")
async def add_skill(skill: Skill):
    with Session(engine) as db:
        db.add(skill)
        db.commit()
        db.refresh(skill)
        return skill

@app.delete("/skills/{id}")
async def del_skill(id:int):
    with Session(engine) as db:
        s=db.exec(select(Skill).where(Skill.id==id)).first()
        if s==None:
            raise HTTPException(status_code=404, detail="id not found")
        db.delete(s)
        db.commit()
        return{"message":"Skill deleted"}

