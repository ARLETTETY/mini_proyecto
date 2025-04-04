from fastapi import FastAPI
from src.routes.holiday import router_holiday
from src.routes.combination_rule import router as router_combination_rule
from src.routes.combination_rule_r_schedule_deviation_rule import router as router_combination_rule_r
from src.routes.schedule_deviation_rule import router as router_schedule_deviation
from src.config.database import engine, Base
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Incluir los routers de cada módulo

app.include_router(router_holiday, prefix="/api")
app.include_router(router_combination_rule, prefix="/api")
app.include_router(router_combination_rule_r, prefix="/api")
app.include_router(router_schedule_deviation, prefix="/api")

@app.get("/")
def root():
    return {"message": "API de Feriados en FastAPI"}

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
