from pydantic import BaseModel, ConfigDict
from typing import Optional

class ScheduleDeviationRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    before_shift: bool
    after_shift: bool
    requires_approval: bool
    unplanned: bool

class ScheduleDeviationRuleCreate(ScheduleDeviationRuleBase):
    pass

class ScheduleDeviationRuleResponse(ScheduleDeviationRuleBase):
    schedule_deviation_id: int

    model_config = ConfigDict(from_attributes=True)
