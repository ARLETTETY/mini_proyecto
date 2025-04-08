from sqlalchemy.orm import Session
from src.models.holiday import Holiday
from src.schemas.holiday import HolidayCreate, HolidayUpdate

# Obtiene todos los feriados
def get_feriados(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Holiday).offset(skip).limit(limit).all()

# Obtiene un feriado por ID
def get_feriado_by_id(db: Session, holiday_id: int):
    return db.query(Holiday).filter(Holiday.holiday_id == holiday_id).first()

# Obtiene un feriado por fecha
def create_feriado(db: Session, feriado_data: HolidayCreate):
    db_feriado = Holiday(**feriado_data.model_dump())
    db.add(db_feriado)
    db.commit()
    db.refresh(db_feriado)
    return db_feriado

# Obtiene un feriado por fecha
def update_feriado(db: Session, holiday_id: int, feriado_data: HolidayUpdate):
    db_feriado = db.query(Holiday).filter(Holiday.holiday_id == holiday_id).first()
    if not db_feriado:
        return None
    for key, value in feriado_data.model_dump(exclude_unset=True).items():
        setattr(db_feriado, key, value)
    db.commit()
    db.refresh(db_feriado)
    return db_feriado

# Elimina un feriado por ID
def delete_feriado(db: Session, holiday_id: int):
    db_feriado = db.query(Holiday).filter(Holiday.holiday_id == holiday_id).first()
    if not db_feriado:
        return None
    db.delete(db_feriado)
    db.commit()
    return db_feriado
