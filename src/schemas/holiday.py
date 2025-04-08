from datetime import datetime
import logging
from typing import Optional
from iso3166 import countries_by_alpha2, countries
from pydantic import BaseModel, Field, ConfigDict, field_validator

# Valida los atributos y los convierte a los tipos correctos
class HolidayBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    public_name: str = Field(..., min_length=2, max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    country: str
    is_renounceable: bool = False
    is_local: bool = False
    start: datetime
    end: datetime
    enable: bool = True

    @field_validator("country")
    @classmethod
    def validate_country(cls, v):
        if len(v) != 2 or v.upper() not in countries:
            raise ValueError("El país especificado no es un código ISO 3166-1 alpha-2 válido")
        return v.upper()

# Para crear un nuevo registro
class HolidayCreate(HolidayBase):
    pass

# Para devolver un registro
class HolidayUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    public_name: Optional[str] = Field(None, min_length=2, max_length=100)
    year: Optional[int] = Field(None, ge=1900, le=2100)
    country: Optional[str] = None
    is_renounceable: Optional[bool] = None
    is_local: Optional[bool] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    enable: Optional[bool] = None

    @field_validator("country")
    @classmethod
    def validate_country(cls, v):
        if v:
            try:
                _ = countries.get(v).name
            except Exception as e:
                logging.exception(e)
                raise ValueError("El país especificado no es válido")
        return v


# Para devolver un registro
class HolidayResponse(HolidayBase):
    holiday_id: int

    model_config = ConfigDict(from_attributes=True)
