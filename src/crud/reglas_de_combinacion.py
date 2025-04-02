from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.combinacion import CombinationRule
from src.schemas.combinacion import CombinationRuleCreate, CombinationRuleResponse

router = APIRouter()

# definición de la ruta para las reglas de combinacion
@router.post("/", response_model=CombinationRuleResponse) # define el endpoint con el metodo POST para crear una nueva regla de combinacion

# función para crear una nueva regla de combinación
def create_combination_rule(rule: CombinationRuleCreate, db: Session = Depends(get_db)):
    new_rule = CombinationRule(**rule.model_dump()) # desempaqueta el modelo de la regla de combinacion
    db.add(new_rule) # agrega la nueva regla a la base de datos
    db.commit() # confirma los cambios en la base de datos
    db.refresh(new_rule) # actualiza el objeto con los datos de la base de datos
    return new_rule # devuelve la nueva regla de combinacion creada

# definición de la ruta para obtener todas las reglas de combinacion
@router.get("/", response_model=list[CombinationRuleResponse]) # define el endpoint con el metodo GET para obtener todas las reglas de combinacion
# función para obtener todas las reglas de combinacion
def get_combination_rules(db: Session = Depends(get_db)): 
    return db.query(CombinationRule).all() # devuelve todas las reglas de combinacion de la base de datos

# definición de la ruta para obtener una regla de combinacion por su ID
@router.get("/{rule_id}", response_model=CombinationRuleResponse)

# función para obtener una regla de combinacion por su ID
def get_combination_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(CombinationRule).filter(CombinationRule.combination_rule_id == rule_id).first() # busca la regla de combinacion por su ID en la base de datos
    if not rule: # si no se encuentra la regla de combinacion
        raise HTTPException(status_code=404, detail="Combination Rule not found") # lanza una excepcion HTTP 404
    return rule # devuelve la regla de combinacion encontrada
