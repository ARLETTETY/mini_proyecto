# Configuración de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

# Cargar variables de entorno desde .env
load_dotenv() 
DATABASE_URL = os.getenv("DATABASE_URL")  

class Base(DeclarativeBase):  
    pass

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()