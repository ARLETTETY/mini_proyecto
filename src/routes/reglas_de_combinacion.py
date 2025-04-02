from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.reglas_de_combinacion import ReglasDeCombinacion
from src.schemas.reglas_de_combinacion import ReglasDeCombinacionCreate, ReglasDeCombinacionResponse

router = APIRouter(prefix="/reglas_de_combinacion", tags=["Reglas de Combinacion"]) # crea un enrutador para la API con el prefijo y las etiquetas especificadas

# definición de la ruta para las ReglasDeCombinacion
@router.post("/", response_model=ReglasDeCombinacionResponse)

# función para crear una nueva ReglasDeCombinacion
def create_combination_rule_mapping(rule: ReglasDeCombinacionCreate, db: Session = Depends(get_db)):
    new_rule_mapping = ReglasDeCombinacion(**rule.model_dump()) # desempaqueta el modelo de la regla de combinacion
    db.add(new_rule_mapping) # agrega la nueva regla a la base de datos
    db.commit() # confirma los cambios en la base de datos
    db.refresh(new_rule_mapping) # actualiza el objeto con los datos de la base de datos
    return new_rule_mapping # devuelve la nueva regla de combinacion creada

# definición de la ruta para obtener una ReglasDeCombinacion por su ID
@router.get("/", response_model=list[ReglasDeCombinacionResponse])

# función para obtener todas las ReglasDeCombinacion
def get_combination_rule_mappings(db: Session = Depends(get_db)):
    return db.query(ReglasDeCombinacion).all() # devuelve todas las reglas de combinacion de la base de datos
