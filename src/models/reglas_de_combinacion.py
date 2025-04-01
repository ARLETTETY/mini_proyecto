from sqlalchemy import Column, String, Integer,Boolean,DateTime
from sqlalchemy.orm import Mapped
from src.config.database import Base
from src.models.combinacion import CombinationRule
from src.models.desviacion_de_horario import ScheduleDeviation
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class ReglasDeCombinacion(Base):
    __tablename__ = "combination_rules"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    combination_rule_id: Mapped[int] = Column(Integer, ForeignKey("combination.combination_rule_id"))
    schedule_deviation_id: Mapped[int] = Column(Integer, ForeignKey("schedule_deviation.schedule_deviation_id"))

    # relaciones
    combination_rule = relationship("CombinationRule", back_populates="rules")
    schedule_deviation = relationship("ScheduleDeviation", back_populates="rules")