# Esquemas Pydantic
#Se usa para validar los datos que se envían a la API y para documentar la API.
#es decir entradas y salidas de la API
# vale decir, validar los datos que se reciben de los endpoints (paths/rutas)

from datetime import datetime
import logging
from typing import Optional
from iso3166 import countries
from pydantic import BaseModel, field_validator, ConfigDict, Field


class FeriadoBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)
    public_name: str = Field(..., min_length=3, max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    country: str = Field(..., min_length=2, max_length=2) #codigo del país US,CL,PE...   
    is_renounceable: bool
    is_local: bool
    start: datetime
    end: datetime
    enable: Optional[bool] = True

    @field_validator("country")
    def validate_country(cls, v):
        """Valida que el país ingresado sea un código ISO 3166 válido."""
        try:
            _ = countries.get(v).name
        except Exception as e:
            logging.exception(e)
            raise ValueError("El país especificado no es válido")
        return v


class FeriadoCreate(FeriadoBase):
    """Modelo para la creación de feriados."""
    pass

class FeriadoUpdate(BaseModel):
    """Modelo para actualización de feriados (todos los campos opcionales)."""
    name: Optional[str] = None
    public_name: Optional[str] = None
    year: Optional[int] = None
    country: Optional[str] = None
    is_renounceable: Optional[bool] = None
    is_local: Optional[bool] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    enable: Optional[bool] = None

    @field_validator("country")
    def validate_country(cls, v):
        if v:
            try:
                _ = countries.get(v).name
            except Exception as e:
                logging.exception(e)
                raise ValueError("El país especificado no es válido")
        return v


class FeriadoResponse(FeriadoBase):
    """Modelo para la respuesta de feriados con ID."""
    holiday_id: int

class FeriadoResponse_(BaseModel):
    """Modelo para la respuesta de feriados con ID."""
    holiday_id: int

    model_config = ConfigDict(from_attributes=True)