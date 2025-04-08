from sqlalchemy.orm import Session
from src.models.combination_rule import CombinationRule
from src.schemas.combination_rule import CombinationRuleCreate

# Obtiene todas las combinaciones
def get_combination_rules(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CombinationRule).offset(skip).limit(limit).all()

# Obtiene una combinación por ID
def get_combination_by_id(db: Session, combination_id: int):
    return db.query(CombinationRule).filter(CombinationRule.combination_rule_id == combination_id).first()

# Crea una nueva combinación
def create_combination(db: Session, combination_data: CombinationRuleCreate):
    db_combination = CombinationRule(**combination_data.model_dump())
    db.add(db_combination)
    db.commit()
    db.refresh(db_combination)
    return db_combination
