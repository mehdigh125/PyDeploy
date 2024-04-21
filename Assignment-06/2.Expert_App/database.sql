--sqlcmd -S localhost -U sa
--pas=GHH----
create database todo_db
go

use todo_db
go

if not exists (select * from sysobjects where name='tasks' and xtype='U')
    create table todo_db.dbo.tasks (
	id int IDENTITY(1,1) NOT NULL,
	title nvarchar(20) NULL,
	description nvarchar(60)  NULL,
	[time] nvarchar(20) NULL,
	status int NULL,
	PRIMARY KEY (id)
)
go

INSERT INTO todo_db.dbo.tasks VALUES ('test','test','test',1)
go 3