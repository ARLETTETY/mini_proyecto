from sqlalchemy import Column, SmallInteger, String, Integer,Boolean,DateTime
from sqlalchemy.orm import Mapped, validates
from datetime import datetime
from src.config.database import Base
from iso3166 import countries

# Modelos con SQLAlchemy
# tabla para la base de datos, 
# se define el nombre de la tabla y sus columnas

class Feriado(Base):
    __tablename__ = "feriado"
    
    holiday_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    public_name: Mapped[str] = Column(String)
    year: Mapped[int] = Column(SmallInteger)
    country: Mapped[str] = Column(String)
    is_renounceable: Mapped[bool] = Column(Boolean)
    is_local: Mapped[bool] = Column(Boolean)
    start: Mapped[datetime] = Column(DateTime)
    end: Mapped[datetime] = Column(DateTime)
    enable: Mapped[bool] = Column(Boolean, default=True)

#esto es por si en la lista de paises de iso3166 no se encuentra el pais
# y no se guarde en la base de datos
    @validates("country")
    def validate_country(self, key, value):
        if value and value not in countries:
            raise ValueError(f"El país '{value}' no es válido.")
        return value