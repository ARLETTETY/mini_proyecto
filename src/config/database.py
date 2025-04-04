#configuración de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
load_dotenv()  # Cargar variables de entorno desde .env

DATABASE_URL = os.getenv("DATABASE_URL")  # Cambia a PostgreSQL o MySQL si necesitas

class Base(DeclarativeBase):  # Esta debe ser la única definición de Base
    pass

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()