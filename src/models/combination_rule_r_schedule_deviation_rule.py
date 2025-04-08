from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from src.config.database import Base

class CombinationRuleRScheduleDeviationRule(Base):
    __tablename__ = "combination_rule_r_schedule_deviation_rule"  

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    combination_rule_id: Mapped[int] = Column(Integer, ForeignKey("combination_rule.combination_rule_id"))
    schedule_deviation_id: Mapped[int] = Column(Integer, ForeignKey("schedule_deviation_rule.schedule_deviation_id"))

    # Relaciones bidireccionales
    # combination_rule = relationship("CombinationRule", back_populates="rules")
    # schedule_deviation = relationship("ScheduleDeviationRule", back_populates="rules")

