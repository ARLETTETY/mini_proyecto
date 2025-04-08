import pytest
from fastapi.testclient import TestClient
from main import app  
from src.models import CombinationRule


# Prueba para crear una nueva CombinationRule
def test_create_combination_rule(client: TestClient, db_session):   
    
    data = {
        "name": "Combinación Test",
        "description": "Descripción de prueba",
        "default": False
    }
    response = client.post("/api/combination_rules", json=data)
    print("Response:", response.json())
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]
    assert response.json()["description"] == data["description"]
    assert response.json()["default"] == data["default"]

# Prueba para obtener todas las CombinationRules
def test_get_combination_rules(client: TestClient, db_session):
    
    response = client.get("/api/combination_rules")
    assert response.status_code == 200
    assert isinstance(response.json(), list)