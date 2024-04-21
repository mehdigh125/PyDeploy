from sqlalchemy.orm import relationship
from sqlalchemy import Column,ForeignKey,Integer,NVARCHAR,Identity,Float,Boolean
import database



class Student(database.Base):
    __tablename__ = "students"
    id=Column(Integer,Identity(1,1),primary_key=True)
    firstname=Column(NVARCHAR(20))
    lastname=Column(NVARCHAR(30))
    average=Column(Float)
    graduated=Column(Boolean)
    courses=relationship("Course")
   

class Course(database.Base):
    __tablename__ = "courses"
    id=Column(Integer,Identity(1,1),primary_key=True)
    name=Column(NVARCHAR(30))
    unit=Column(Integer)
    owner_id = Column(Integer, ForeignKey("students.id"))
    owner = relationship("Student")
    



