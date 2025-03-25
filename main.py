from fastapi import FastAPI
from src.routes import feriado
from src.config.database import engine, Base
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# incluye todas las rutas de la API
app.include_router(feriado.router)

@app.get("/")
def root():
    return {"message": "API de Feriados en FastAPI"}
