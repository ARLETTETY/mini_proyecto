import pytest
from fastapi.testclient import TestClient
from main import app
from src.models import CombinationRule, ScheduleDeviationRule, CombinationRuleRScheduleDeviationRule

# Prueba para crear una nueva regla de combinación
def test_create_regla_de_combinacion(client: TestClient, db_session):

    # Se insertan datos de prueba necesarios para la prueba

    rule =  CombinationRule(name= "Regla test")
    deviation = ScheduleDeviationRule(
        name= "Desviación test", 
        description="Descripción test", 
        before_shift=True, 
        after_shift=False, 
        requires_approval=True, 
        unplanned=False)

    db_session.add(rule)
    db_session.add(deviation)
    db_session.commit()

    data = {
        "combination_rule_id": rule.combination_rule_id,  
        "schedule_deviation_id": deviation.schedule_deviation_id,
    }

    response = client.post("/api/combination_rule_r_schedule_deviation_rule", json=data)
    assert response.status_code == 200
    assert response.json()["combination_rule_id"] == rule.combination_rule_id
    assert response.json()["schedule_deviation_id"] == deviation.schedule_deviation_id
    


def test_get_reglas_de_combinacion(client: TestClient, db_session):
   
    # Se insertan dependecias necesarias para la prueba
    rule =  CombinationRule(name= "Regla test")
    deviation = ScheduleDeviationRule(
        name= "Desviación test", 
        description="Descripción test", 
        before_shift=True, 
        after_shift=False, 
        requires_approval=True, 
        unplanned=False)
    
    db_session.add_all([rule, deviation])
    db_session.commit()

    combinacion = CombinationRuleRScheduleDeviationRule(
        combination_rule_id=rule.combination_rule_id,
        schedule_deviation_id=deviation.schedule_deviation_id)
    
    db_session.add(combinacion)
    db_session.commit()
    
    response = client.get("/api/combination_rule_r_schedule_deviation_rule")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica que es una lista
    assert len(response.json()) > 0  # Asegura que haya datos en la respuesta
