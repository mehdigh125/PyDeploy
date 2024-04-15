from fastapi import FastAPI,File,Form,UploadFile,HTTPException
import pymssql
import dotenv
import os

dotenv = dotenv.load_dotenv()
passql = os.getenv("passql") 
app=FastAPI()


conn = pymssql.connect(host='denali.liara.cloud', user='sa', password=passql, database='todo_db',port=32953)
cursor = conn.cursor()


@app.get("/")
def read_root():
    return "Hi, welcome to my api In this api there is  requests for read, add, update and remove database--created by mehdi ghaffari moghaddam"

@app.get("/items")
def read_data():
    data={}
    j=0
    cursor.execute('SELECT * FROM tasks order by id')
    for i in cursor:
        data[j]=i
        j=j+1
    return(str(data))

@app.post("/items")
def insert_data(title: str=Form(),description:str=Form(),time:str=Form(),status:int=Form()):
    sql_command="insert into tasks(title,description,time,status) values(%s,%s,%s,%d)"
    val=(title,description,time,status)
    cursor.execute(sql_command,val)
    conn.commit()
    cursor.execute('SELECT * FROM tasks ORDER BY ID DESC')
    myresult = cursor.fetchone()
    return(str(myresult))
    

@app.delete("/items/{id}")
def remove_data(id:str):
     cursor.execute('SELECT COUNT(id) FROM tasks  where id='+id)
     result = cursor.fetchone()
     row_count = result[0]
     if row_count==0:
        raise HTTPException(status_code=404, detail="Item not found")
     sql_command = "delete from  tasks  where id="+id
     cursor.execute(sql_command)
     conn.commit()

@app.put("/items/{id}")
def update_data(id:str,title: str=Form(),description:str=Form(),time:str=Form(),status:int=Form()):

    cursor.execute('SELECT COUNT(id) FROM tasks  where id='+id)
    result = cursor.fetchone()
    row_count = result[0]
    if row_count==0:
        raise HTTPException(status_code=404, detail="Item not found")
    
 
    sql_command=("UPDATE tasks SET title =%s,description=%s,time=%s,status=%d WHERE id="+id)
    val=(title,description,time,status)
    cursor.execute(sql_command,val)
    conn.commit()