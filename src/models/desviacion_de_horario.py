from sqlalchemy import Column, String, Integer,Boolean,DateTime
from sqlalchemy.orm import Mapped
from src.config.database import Base
from sqlalchemy.orm import relationship

class ScheduleDeviation(Base):
    __tablename__ = "schedule_deviation"  

    schedule_deviation_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True)
    description: Mapped[str] = Column(String)
    before_shift: Mapped[bool] = Column(Boolean)
    after_shift: Mapped[bool] = Column(Boolean)  
    requires_approval: Mapped[bool] = Column(Boolean)  
    unplanned: Mapped[bool] = Column(Boolean)

    # relación con ReglasDeCombinacion
    rules = relationship("ReglasDeCombinacion", back_populates="schedule_deviation")
