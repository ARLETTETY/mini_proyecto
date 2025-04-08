from pydantic import BaseModel, ConfigDict
from typing import Optional

# Valida los atributos y los convierte a los tipos correctos
class ScheduleDeviationRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    before_shift: bool
    after_shift: bool
    requires_approval: bool
    unplanned: bool

# Para crear un nuevo registro
class ScheduleDeviationRuleCreate(ScheduleDeviationRuleBase):
    pass

# Para devolver un registro
class ScheduleDeviationRuleResponse(ScheduleDeviationRuleBase):
    schedule_deviation_id: int

    model_config = ConfigDict(from_attributes=True)
