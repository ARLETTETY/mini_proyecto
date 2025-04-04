from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import Mapped
from src.config.database import Base
from sqlalchemy.orm import relationship

class CombinationRule(Base):
    __tablename__ = "combination"   

    combination_rule_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True)
    description: Mapped[str] = Column(String)
    default: Mapped[bool] = Column(Boolean)

    # Relación con ReglasDeCombinacion (hacia atrás)
    rules = relationship("ReglasDeCombinacion", back_populates="combination")

