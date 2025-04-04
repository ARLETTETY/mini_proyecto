from pydantic import BaseModel, ConfigDict
from typing import Optional

class CombinationRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    default: bool

class CombinationRuleCreate(CombinationRuleBase):
    pass

class CombinationRuleResponse(CombinationRuleBase):
    combination_rule_id: int

    model_config = ConfigDict(from_attributes=True)
