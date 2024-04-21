from sqlalchemy.orm import Session

import models 



def read_student(id:int,db:Session):
    return db.query(models.Student).filter(models.Student.id==id).first()

def read_course(id:int,db:Session):
    return db.query(models.Course).filter(models.Course.id==id).first()


def create_student(firstname:str,lastname:str,average:float,graduated:bool,db:Session):
    student=models.Student(firstname=firstname,lastname=lastname,average=average,graduated=graduated)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def create_course(name:str,unit:int,owner_id:int,db:Session):
    course=models.Course(name=name,unit=unit,owner_id=owner_id)
    
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def remove_student(student,db:Session):
    db.delete(student)
    db.commit()
    return{"message":"student deleted successfully"}  

def remove_course(course,db:Session):
    db.delete(course)
    db.commit()
    return{"message":"course deleted successfully"}  



def update_student(student,firstname:str,lastname:str,average:float,graduated:bool,db:Session):
    student.firstname=firstname
    student.lastname=lastname
    student.average=average
    student.graduated=graduated
    db.commit()
    db.refresh(student)
    return student

def update_course(course,name:str,unit:int,owner_id:int,db:Session):
    course.name=name
    course.unit=unit
    course.owner_id=owner_id
    db.commit()
    db.refresh(course)
    return course