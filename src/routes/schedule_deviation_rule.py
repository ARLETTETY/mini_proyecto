from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.crud.schedule_deviation_rule import get_schedule_deviations, get_schedule_deviation_by_id, create_schedule_deviation
from src.schemas.schedule_deviation_rule import ScheduleDeviationRuleCreate, ScheduleDeviationRuleResponse

router = APIRouter(prefix="/schedule_deviations", tags=["Schedule Deviations"])

# Obtener todas las desviaciones de horario
@router.get("/", response_model=list[ScheduleDeviationRuleResponse])
def read_schedule_deviations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_schedule_deviations(db, skip, limit)

# Obtener una desviación de horario por ID
@router.get("/{schedule_deviation_id}", response_model=ScheduleDeviationRuleResponse)
def read_schedule_deviation(schedule_deviation_id: int, db: Session = Depends(get_db)):
    schedule_deviation = get_schedule_deviation_by_id(db, schedule_deviation_id)
    if not schedule_deviation:
        raise HTTPException(status_code=404, detail="Schedule Deviation not found")
    return schedule_deviation

# Crear una nueva desviación de horario
@router.post("/", response_model=ScheduleDeviationRuleResponse)
def create_new_schedule_deviation(schedule_deviation_data: ScheduleDeviationRuleCreate, db: Session = Depends(get_db)):
    return create_schedule_deviation(db, schedule_deviation_data)
