from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv
import os
import urllib

dotenv = dotenv.load_dotenv()
passql = os.getenv("passql") 


connection_string = "DRIVER={ODBC Driver 17 for SQL Server};TrustServerCertificate=yes;Database=todo_db;SERVER=mssql;UID=sa;PWD=Lllw95u35UIYutJIMH02nsoF"

connection_string = urllib.parse.quote_plus(connection_string) 
connection_string = "mssql:///?odbc_connect=%s" % connection_string



engine = create_engine(connection_string)
con=engine.connect()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()