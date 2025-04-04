from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import Mapped, relationship
from src.config.database import Base

class ScheduleDeviationRule(Base):
    __tablename__ = "schedule_deviation_rule"  

    schedule_deviation_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True)
    description: Mapped[str] = Column(String)
    before_shift: Mapped[bool] = Column(Boolean)
    after_shift: Mapped[bool] = Column(Boolean)  
    requires_approval: Mapped[bool] = Column(Boolean)  
    unplanned: Mapped[bool] = Column(Boolean)

    # Relación con la tabla intermedia
    rules = relationship("CombinationRuleRScheduleDeviationRule", back_populates="schedule_deviation")
