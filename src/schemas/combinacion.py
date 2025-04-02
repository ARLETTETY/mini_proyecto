from pydantic import BaseModel
from typing import Optional

#valida que los atributos ingresados sean correctos y los convierte a los tipos de datos correctos
class CombinationRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    default: bool

#para crear un nuevo registro de regla de combinacion que se le pase al endpoint  se utiliza el modelo CombinationRuleCreate
class CombinationRuleCreate(CombinationRuleBase):
    pass

#para devolver el registro de regla de combinacion que se le pase al endpoint se utiliza el modelo CombinationRuleResponse
class CombinationRuleResponse(CombinationRuleBase):
    combination_rule_id: int

    class Config:
        #permite de un sqlalchemy a un pydantic, lo que permite que los atributos de la clase sean los mismos que los de la tabla de la base de datos
        from_attributes = True 