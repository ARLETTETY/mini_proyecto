from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemas.holiday import HolidayResponse, HolidayUpdate, HolidayCreate
from src.crud.holiday import (
    get_feriados, get_feriado_by_id, create_feriado, update_feriado, delete_feriado
)

router_holiday = APIRouter(prefix="/holiday", tags=["Feriados"])

@router_holiday.get("/", response_model=list[HolidayResponse])
def read_feriados(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_feriados(db, skip, limit)

@router_holiday.get("/{holiday_id}", response_model=HolidayResponse)
def read_feriado(holiday_id: int, db: Session = Depends(get_db)):
    db_feriado = get_feriado_by_id(db, holiday_id)
    if db_feriado is None:
        raise HTTPException(status_code=404, detail="Feriado no encontrado")
    return db_feriado

@router_holiday.post("/", response_model=HolidayResponse, status_code=201)
def create_new_feriado(feriado: HolidayCreate, db: Session = Depends(get_db)):
    return create_feriado(db, feriado)

@router_holiday.put("/{holiday_id}", response_model=HolidayResponse)
def update_existing_feriado(holiday_id: int, feriado: HolidayUpdate, db: Session = Depends(get_db)):
    updated_feriado = update_feriado(db, holiday_id, feriado)
    if updated_feriado is None:
        raise HTTPException(status_code=404, detail="Feriado no encontrado")
    return updated_feriado

@router_holiday.delete("/{holiday_id}")
def delete_existing_feriado(holiday_id: int, db: Session = Depends(get_db)):
    deleted_feriado = delete_feriado(db, holiday_id)
    if deleted_feriado is None:
        raise HTTPException(status_code=404, detail="Feriado no encontrado")
    return {"message": "Feriado eliminado"}
