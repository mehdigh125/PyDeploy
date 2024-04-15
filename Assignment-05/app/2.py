
import pymssql



conn = pymssql.connect(host='172.25.23.94', user='sa', password='GHH1400@', database='todo_db',port=1433)
cursor = conn.cursor()


#update
sql_command=("UPDATE tasks SET title = %s,description= %s,time= %s,status= %s WHERE id =8")
val=('10','20','30','40')
cursor.execute(sql_command,val)
conn.commit()


#insert

# sql_command=("insert into tasks(title,description,time,status) values(%s,%s,%s,%s)")
# val=('10','20','30','40')
# cursor.execute(sql_command,val)
# conn.commit()

data={}
j=0
cursor.execute('SELECT * FROM tasks order by id')
for i in cursor:
    data[j]=i
    j=j+1
print(str(data))