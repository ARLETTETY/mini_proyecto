#endpoints de la api 

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemas.feriado import FeriadoCreate, FeriadoUpdate, FeriadoResponse
from src.crud.feriado import (
    get_feriados, get_feriado_by_id, create_feriado, update_feriado, delete_feriado
)

router = APIRouter(prefix="/feriados", tags=["Feriados"])

@router.get("/", response_model=list[FeriadoResponse])
def read_feriados(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_feriados(db, skip, limit)

@router.get("/{holiday_id}", response_model=FeriadoResponse)
def read_feriado(holiday_id: int, db: Session = Depends(get_db)):
    db_feriado = get_feriado_by_id(db, holiday_id)
    if db_feriado is None:
        raise HTTPException(status_code=404, detail="Feriado no encontrado")
    return db_feriado

@router.post("/", response_model=FeriadoResponse)
def create_new_feriado(feriado: FeriadoCreate, db: Session = Depends(get_db)):
    return create_feriado(db, feriado)

@router.put("/{holiday_id}", response_model=FeriadoResponse)
def update_existing_feriado(holiday_id: int, feriado: FeriadoUpdate, db: Session = Depends(get_db)):
    updated_feriado = update_feriado(db, holiday_id, feriado)
    if updated_feriado is None:
        raise HTTPException(status_code=404, detail="Feriado no encontrado")
    return updated_feriado

@router.delete("/{holiday_id}")
def delete_existing_feriado(holiday_id: int, db: Session = Depends(get_db)):
    deleted_feriado = delete_feriado(db, holiday_id)
    if deleted_feriado is None:
        raise HTTPException(status_code=404, detail="Feriado no encontrado")
    return {"message": "Feriado eliminado"}
