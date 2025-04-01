from pydantic import BaseModel

#valida que los atributos ingresados sean correctos y los convierte a los tipos de datos correctos
class ReglasDeCombinacionBase(BaseModel):
    combination_rule_id: int
    schedule_deviation_id: int

#para crear un nuevo registro de regla de combinacion que se le pase al endpoint  se utiliza el modelo ReglasDeCombinacionCreate
class ReglasDeCombinacionCreate(ReglasDeCombinacionBase):
    pass

#para devolver el registro de regla de combinacion que se le pase al endpoint se utiliza el modelo ReglasDeCombinacionResponse
class ReglasDeCombinacionResponse(ReglasDeCombinacionBase):
    id: int

    class Config:
         #permite de un sqlalchemy a un pydantic, lo que permite que los atributos de la clase sean los mismos que los de la tabla de la base de datos
        from_attributes = True