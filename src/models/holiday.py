from sqlalchemy import Column, SmallInteger, String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, validates
from datetime import datetime
from src.config.database import Base
from iso3166 import countries

class Holiday(Base):
    __tablename__ = "feriado"
    
    holiday_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, nullable=False)
    public_name: Mapped[str] = Column(String, nullable=False)
    year: Mapped[int] = Column(SmallInteger, nullable=False)
    country: Mapped[str] = Column(String, nullable=False)
    is_renounceable: Mapped[bool] = Column(Boolean, default=False)
    is_local: Mapped[bool] = Column(Boolean, default=False)
    start: Mapped[datetime] = Column(DateTime, nullable=False)
    end: Mapped[datetime] = Column(DateTime, nullable=False)
    enable: Mapped[bool] = Column(Boolean, default=True)

    @validates("country")
    def validate_country(self, key, value):
        if value and value not in countries:
            raise ValueError(f"El país '{value}' no es válido.")
        return value
