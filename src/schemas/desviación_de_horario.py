from pydantic import BaseModel
from typing import Optional

#valida que los atributos ingresados sean correctos y los convierte a los tipos de datos correctos
class ScheduleDeviationBase(BaseModel):
    name: str
    description: Optional[str] = None #el campo description es opcional
    before_shift: bool
    after_shift: bool
    requires_approval: bool
    unplanned: bool

#para crear un nuevo registro de desviación de horario que se le pase al endpoint  se utiliza el modelo ScheduleDeviationCreate
class ScheduleDeviationCreate(ScheduleDeviationBase):
    pass

#para devolver el registro de desviación de horario que se le pase al endpoint se utiliza el modelo ScheduleDeviationResponse
class ScheduleDeviationResponse(ScheduleDeviationBase):
    schedule_deviation_id: int

    class Config:
        #permite de un sqlalchemy a un pydantic, lo que permite que los atributos de la clase sean los mismos que los de la tabla de la base de datos
        from_attributes = True 
