#configuración de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

DATABASE_URL = os.getenv("DATABASE_URL")  # Cambia a PostgreSQL o MySQL si necesitas


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
#dependencia de la base de datos para inyectar en los endpoints

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()