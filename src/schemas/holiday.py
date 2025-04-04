from datetime import datetime
import logging
from typing import Optional
from iso3166 import countries
from pydantic import BaseModel, field_validator, ConfigDict

class FeriadoBase(BaseModel):
    name: str
    public_name: str
    year: int
    country: str
    is_renounceable: bool = False
    is_local: bool = False
    start: datetime
    end: datetime
    enable: bool = True

    @field_validator("country")
    def validate_country(cls, v):
        try:
            _ = countries.get(v).name
        except Exception as e:
            logging.exception(e)
            raise ValueError("El país especificado no es válido")
        return v

class FeriadoCreate(FeriadoBase):
    pass

class FeriadoUpdate(BaseModel):
    name: Optional[str] = None
    public_name: Optional[str] = None
    year: Optional[int] = None
    country: Optional[str] = None
    is_renounceable: Optional[bool] = None
    is_local: Optional[bool] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    enable: Optional[bool] = None

class FeriadoResponse(FeriadoBase):
    holiday_id: int

    model_config = ConfigDict(from_attributes=True)
