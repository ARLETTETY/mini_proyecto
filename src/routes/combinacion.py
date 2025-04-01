from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.combinacion import CombinationRule
from src.schemas.combinacion import CombinationRuleCreate, CombinationRuleResponse

router = APIRouter(prefix="/combinacion", tags=["Combinacion"]) # crea un enrutador para la API con el prefijo y las etiquetas especificadas

# definición de la ruta para las reglas de combinacion
@router.post("/", response_model=CombinationRuleResponse)

# función para crear una nueva regla de combinación
def create_combination_rule(rule: CombinationRuleCreate, db: Session = Depends(get_db)):
    new_rule = CombinationRule(**rule.model_dump()) # desempaqueta el modelo de la regla de combinacion
    db.add(new_rule) # agrega la nueva regla a la base de datos
    db.commit() # confirma los cambios en la base de datos
    db.refresh(new_rule) # actualiza el objeto con los datos de la base de datos
    return new_rule # devuelve la nueva regla de combinacion creada

# definición de la ruta para obtener todas las reglas de combinacion
@router.get("/", response_model=list[CombinationRuleResponse])

# función para obtener todas las reglas de combinacion
def get_combination_rules(db: Session = Depends(get_db)): 
    return db.query(CombinationRule).all() # devuelve todas las reglas de combinacion de la base de datos
