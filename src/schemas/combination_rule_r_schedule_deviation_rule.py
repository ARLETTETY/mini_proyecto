from pydantic import BaseModel, ConfigDict

# Valida los atributos y los convierte a los tipos correctos
class CombinationRuleRScheduleDeviationRuleBase(BaseModel):
    combination_rule_id: int
    schedule_deviation_id: int

# Para crear un nuevo registro
class CombinationRuleRScheduleDeviationRuleCreate(CombinationRuleRScheduleDeviationRuleBase):
    pass

# Para devolver un registro
class CombinationRuleRScheduleDeviationRuleResponse(CombinationRuleRScheduleDeviationRuleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
