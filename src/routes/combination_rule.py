from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.crud.combination_rule import get_combination_rules, get_combination_by_id, create_combination
from src.schemas.combination_rule import CombinationRuleCreate, CombinationRuleResponse

router = APIRouter(prefix="/combination_rules", tags=["Combination Rules"])

# Obtiene todas las combinaciones
@router.get("/", response_model=list[CombinationRuleResponse])
def read_combination_rules(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_combination_rules(db, skip, limit)

# Obtiene una combinación por ID
@router.get("/{combination_id}", response_model=CombinationRuleResponse)
def read_combination(combination_id: int, db: Session = Depends(get_db)):
    combination = get_combination_by_id(db, combination_id)
    if not combination:
        raise HTTPException(status_code=404, detail="Combination not found")
    return combination

# Crea una nueva combinación
@router.post("/", response_model=CombinationRuleResponse)
def create_new_combination(combination_data: CombinationRuleCreate, db: Session = Depends(get_db)):
    return create_combination(db, combination_data)
