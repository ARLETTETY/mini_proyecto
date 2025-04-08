from pydantic import BaseModel, ConfigDict
from typing import Optional

# Valida los atributos y los convierte a los tipos correctos
class CombinationRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    default: bool

# Para crear un nuevo registro
class CombinationRuleCreate(CombinationRuleBase):
    pass

# Para devolver un registro
class CombinationRuleResponse(CombinationRuleBase):
    combination_rule_id: int

    model_config = ConfigDict(from_attributes=True)
