import pytest
from fastapi.testclient import TestClient
from main import app  
from src.models import ScheduleDeviationRule

# Prueba para crear una nueva ScheduleDeviationRule
def test_create_schedule_deviation(client: TestClient):
    data = {
        "name": "Desviación Test",
        "description": "Descripción test",
        "before_shift": True,
        "after_shift": False,
        "requires_approval": False,
        "unplanned": True
    }
    response = client.post("/api/schedule_deviations", json=data)
    print("Response:", response.json())
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]
    assert response.json()["description"] == data["description"]
    assert response.json()["before_shift"] == data["before_shift"]


# Prueba para obtener todas las ScheduleDeviationRules.
def test_get_schedule_deviations(client: TestClient):
    
    response = client.get("/api/schedule_deviations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)