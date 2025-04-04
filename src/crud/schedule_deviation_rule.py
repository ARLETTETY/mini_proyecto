from sqlalchemy.orm import Session
from src.models.schedule_deviation_rule import ScheduleDeviationRule
from src.schemas.schedule_deviation_rule import ScheduleDeviationRuleCreate

# Obtener todas las desviaciones de horario
def get_schedule_deviations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ScheduleDeviationRule).offset(skip).limit(limit).all()

# Obtener una desviación de horario por ID
def get_schedule_deviation_by_id(db: Session, schedule_deviation_id: int):
    return db.query(ScheduleDeviationRule).filter(ScheduleDeviationRule.schedule_deviation_id == schedule_deviation_id).first()

# Crear una nueva desviación de horario
def create_schedule_deviation(db: Session, schedule_deviation_data: ScheduleDeviationRuleCreate):
    db_schedule_deviation = ScheduleDeviationRule(**schedule_deviation_data.model_dump())
    db.add(db_schedule_deviation)
    db.commit()
    db.refresh(db_schedule_deviation)
    return db_schedule_deviation
