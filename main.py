from fastapi import FastAPI
from src.routes.holiday import router_holiday
from src.routes.combination_rule import router as router_combination_rule
from src.routes.combination_rule_r_schedule_deviation_rule import router as router_combination_rule_r
from src.routes.schedule_deviation_rule import router as router_schedule_deviation
from src.config.database import engine, Base
from dotenv import load_dotenv

# CARGAR VARIABLES DE ENTORNO DESDE EL ARCHIVO .env
load_dotenv()

# Esto crea una instancia de la clase FastAPI. Es el corazón de la app donde se definen rutas, middlewares, configuraciones, etc.
# Con esta instancia (app), se pueden usar decoradores como @app.get(), @app.post() y montar routers con app.include_router().
app = FastAPI()

# Incluir los routers de cada módulo
app.include_router(router_holiday, prefix="/api")
app.include_router(router_combination_rule, prefix="/api")
app.include_router(router_schedule_deviation, prefix="/api")
app.include_router(router_combination_rule_r, prefix="/api")
# CON ESTO SE CREA LA TABLA EN LA BASE DE DATOS
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API de Feriados en FastAPI"}

# print(Base.metadata.tables.keys())
