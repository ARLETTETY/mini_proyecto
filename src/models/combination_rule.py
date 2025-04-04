from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import Mapped, relationship
from src.config.database import Base

class CombinationRule(Base):
    __tablename__ = "combination_rule"  # Nombre corregido

    combination_rule_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True)
    description: Mapped[str] = Column(String)
    default: Mapped[bool] = Column(Boolean)

    # Relación con la tabla intermedia
    rules = relationship("CombinationRuleRScheduleDeviationRule", back_populates="combination_rule")
