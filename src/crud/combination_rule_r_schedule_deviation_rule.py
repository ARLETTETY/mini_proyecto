from sqlalchemy.orm import Session
from src.models.combination_rule_r_schedule_deviation_rule import CombinationRuleRScheduleDeviationRule
from src.schemas.combination_rule_r_schedule_deviation_rule import CombinationRuleRScheduleDeviationRuleCreate

# Obtener todas las reglas de combinación
def get_reglas_de_combinacion(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CombinationRuleRScheduleDeviationRule).offset(skip).limit(limit).all()

# Obtener una regla de combinación por ID
def get_regla_de_combinacion_by_id(db: Session, regla_id: int):
    return db.query(CombinationRuleRScheduleDeviationRule).filter(CombinationRuleRScheduleDeviationRule.id == regla_id).first()

# Crear una nueva regla de combinación
def create_regla_de_combinacion(db: Session, regla_data: CombinationRuleRScheduleDeviationRuleCreate):
    db_regla = CombinationRuleRScheduleDeviationRule(**regla_data.model_dump())
    db.add(db_regla)
    db.commit()
    db.refresh(db_regla)
    return db_regla
