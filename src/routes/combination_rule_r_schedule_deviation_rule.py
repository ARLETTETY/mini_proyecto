from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.crud.combination_rule_r_schedule_deviation_rule import (
    get_reglas_de_combinacion,
    get_regla_de_combinacion_by_id,
    create_regla_de_combinacion,
)
from src.schemas.combination_rule_r_schedule_deviation_rule import (
    CombinationRuleRScheduleDeviationRuleCreate,
    CombinationRuleRScheduleDeviationRuleResponse,
)

router = APIRouter(prefix="/combination_rule_r_schedule_deviation_rule", tags=["Combination Rules - Schedule Deviation"])

# Obtiene todas las reglas de combinación
@router.get("/", response_model=list[CombinationRuleRScheduleDeviationRuleResponse])
def read_reglas_de_combinacion(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_reglas_de_combinacion(db, skip, limit)

# Obtiene una regla de combinación por ID
@router.get("/{regla_id}", response_model=CombinationRuleRScheduleDeviationRuleResponse)
def read_regla_de_combinacion(regla_id: int, db: Session = Depends(get_db)):
    regla = get_regla_de_combinacion_by_id(db, regla_id)
    if not regla:
        raise HTTPException(status_code=404, detail="Regla de combinación no encontrada")
    return regla

# Crea una nueva regla de combinación
@router.post("/", response_model=CombinationRuleRScheduleDeviationRuleResponse)
def create_new_regla_de_combinacion(regla_data: CombinationRuleRScheduleDeviationRuleCreate, db: Session = Depends(get_db)):
    return create_regla_de_combinacion(db, regla_data)
