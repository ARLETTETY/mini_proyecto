from fastapi.testclient import TestClient
from main import app

client = TestClient(app)  # Cliente para pruebas unitarias

def test_create_regla_de_combinacion(client: TestClient):
    """Prueba para crear una nueva regla de combinación."""
    data = {
        "combination_rule_id": 1,
        "schedule_deviation_id": 1
    }
    response = client.post("/api/combination_rule_r_schedule_deviation_rule", json=data)
    assert response.status_code == 200
    assert response.json()["combination_rule_id"] == 1
    assert response.json()["schedule_deviation_id"] == 1

def test_get_reglas_de_combinacion(client: TestClient):
    """Prueba para obtener todas las reglas de combinación."""
    response = client.get("/api/combination_rule_r_schedule_deviation_rule")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica que es una lista
    assert len(response.json()) > 0  # Asegura que haya datos en la respuesta
