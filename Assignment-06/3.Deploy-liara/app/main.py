#import pandas as pd

#import models,crud
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine

from . import crud, models

models.database.Base.metadata.create_all(bind=engine)





app = FastAPI()

def get_db():
    db=SessionLocal()
    yield db
    db.close()

@app.post("/students")
def create_student(firstname:str,lastname:str,average:float,graduated:bool,db:Session=Depends(get_db)):
    return crud.create_student(db=db,firstname=firstname,lastname=lastname,average=average,graduated=graduated)

@app.post("/courses")
def create_course(name:str,unit:int,owner_id:int,db:Session=Depends(get_db)):
    return crud.create_course(db=db,name=name,unit=unit,owner_id=owner_id)



@app.get("/students")
def read_student(id:int,db:Session=Depends(get_db)):
    user=crud.read_student(id,db)
    if user is None:
        raise HTTPException(status_code=404,detail="student not found")
    return user

@app.get("/courses")
def read_course(id:int,db:Session=Depends(get_db)):
    courses=crud.read_course(id,db)
    if courses is None:
        raise HTTPException(status_code=404,detail="course not found")
    return courses

@app.delete("/students/{id}")
def remove_student(id:int,db:Session=Depends(get_db)):
    student=crud.read_student(id,db)
    if student is None:
        raise HTTPException(status_code=404,detail="student not found")    
    return crud.remove_student(student,db)

@app.delete("/courses/{id}")
def remove_course(id:int,db:Session=Depends(get_db)):
    course=crud.read_course(id,db)
    if course is None:
        raise HTTPException(status_code=404,detail="course not found")    
    return crud.remove_course(course,db)




@app.put("/students/{id}")
def update_student(id:int,firstname:str,lastname:str,average:float,graduated:bool,db:Session=Depends(get_db)):
    student=crud.read_student(id,db)
    if student is None:
        raise HTTPException(status_code=404,detail="student not found")    
    return crud.update_student(student,firstname,lastname,average,graduated,db)


@app.put("/courses/{id}")
def update_course(id:int,name:str,unit:int,owner_id:int,db:Session=Depends(get_db)):
    course=crud.read_course(id,db)
    if course is None:
        raise HTTPException(status_code=404,detail="course not found")    
    return crud.update_course(course,name,unit,owner_id,db)


# df=pd.read_sql_query("select * from todo_db.dbo.users",con)
# print(df)