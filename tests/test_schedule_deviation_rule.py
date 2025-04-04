from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)  # Cliente para pruebas unitarias

def test_create_schedule_deviation(client: TestClient):
    """Prueba para crear una nueva desviación de horario."""
    data = {
        "name": "Desviación de horario 1",
        "description": "Descripción de prueba",
        "before_shift": True,
        "after_shift": False,
        "requires_approval": True,
        "unplanned": False
    }
    response = client.post("/api/schedule_deviations", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Desviación de horario 1"
    assert response.json()["description"] == "Descripción de prueba"

def test_get_schedule_deviations(client: TestClient):
    """Prueba para obtener todas las desviaciones de horario."""
    response = client.get("/api/schedule_deviations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica que es una lista
    assert len(response.json()) > 0  # Asegura que haya datos en la respuesta
