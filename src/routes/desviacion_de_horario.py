from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.desviacion_de_horario import ScheduleDeviation
from src.schemas.desviación_de_horario import ScheduleDeviationCreate, ScheduleDeviationResponse

router = APIRouter(prefix="/desviacion_de_hoario", tags=["Desviacion de horario"]) # crea un enrutador para la API con el prefijo y las etiquetas especificadas

# definición de la ruta para las desviaciones de horario
@router.post("/", response_model=ScheduleDeviationResponse)

# función para crear una nueva desviación de horario
def create_schedule_deviation(deviation: ScheduleDeviationCreate, db: Session = Depends(get_db)):
    new_deviation = ScheduleDeviation(**deviation.model_dump()) # desempaqueta el modelo de la desviacion de horario
    db.add(new_deviation) # agrega la nueva desviacion a la base de datos
    db.commit() # confirma los cambios en la base de datos
    db.refresh(new_deviation) # actualiza el objeto con los datos de la base de datos
    return new_deviation # devuelve la nueva desviacion de horario creada

# definición de la ruta para obtener una desviación de horario por su ID
@router.get("/", response_model=list[ScheduleDeviationResponse])

# función para obtener todas las desviaciones de horario
def get_schedule_deviations(db: Session = Depends(get_db)):
    return db.query(ScheduleDeviation).all() # devuelve todas las desviaciones de horario de la base de datos
