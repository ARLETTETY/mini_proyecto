import json
import pytest
from datetime import datetime
from main import app 
from fastapi.testclient import TestClient

client = TestClient(app)  # Cliente para pruebas unitarias

""" @pytest.fixture
def create_test_feriado():
    Crea un feriado antes de ejecutar ciertas pruebas.
    data = {
        "name": "Navidad",
        "public_name": "Día de Navidad",
        "year": 2025,
        "country": "US",
        "is_renounceable": False,
        "is_local": False,
        "start": datetime(2025, 12, 25, 0, 0).isoformat(),
        "end": datetime(2025, 12, 25, 23, 59).isoformat(),
        "enable": True
    }
    response = client.post(prefix, json=data)
    assert response.status_code == 200 # Verifica que la creación fue exitosa
    assert response.json()["name"] == "Navidad"
    return response.json()  # Devuelve el feriado creado para usar en otras pruebas """

""" def test_create_feriado():
    Prueba la creación de un feriado
    data = {
        "name": "Año Nuevo",
        "public_name": "Día de Año Nuevo",
        "year": 2025,
        "country": "US",
        "is_renounceable": False,
        "is_local": False,
        "start": datetime(2025, 1, 1, 0, 0).isoformat(),
        "end": datetime(2025, 1, 1, 23, 59).isoformat(),
        "enable": True
    }
    response = client.post("/api/feriados/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Año Nuevo"
 """
def test_get_feriados():
    """Prueba la obtención de feriados."""
    response = client.get("/api/holiday")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

""" def test_update_feriado(create_test_feriado):
    Prueba la actualización de un feriado existente
    feriado_id = create_test_feriado["holiday_id"]
    update_data = {"name": "Navidad Modificada"}
    response = client.put(f"{prefix}{feriado_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Navidad Modificada"

def test_delete_feriado(create_test_feriado):
    Prueba la eliminación de un feriado
    feriado_id = create_test_feriado["holiday_id"]
    print(feriado_id)
    response = client.delete(f"/api/feriados/{feriado_id}")
    assert response.status_code == 200

    # Verificar que el feriado realmente fue eliminado
    response = client.get(f"/api/feriado/{feriado_id}")
    assert response.status_code == 404  # Debe devolver un 404 porque ya no existe """

""" def test_invalid_name():
    Prueba que falla si el nombre es demasiado corto
    data = {
        "name": "A",  # solo 1 caracter (debe fallar)
        "public_name": "Día de Año Nuevo",
        "year": 2025,
        "country": "US",
        "is_renounceable": False,
        "is_local": False,
        "start": datetime(2025, 1, 1, 0, 0).isoformat(),
        "end": datetime(2025, 1, 1, 23, 59).isoformat(),
        "enable": True
    }
    response = client.post("/api/feriados/", json=data)
    assert response.status_code == 422  # Debe fallar con un 422
    assert "name" in response.json()["detail"][0]["loc"]  # 📌 Verifica el campo con error


def test_invalid_year():
    Prueba que falla si el año no está en el rango válido
    data = {
        "name": "Año Nuevo",
        "public_name": "Día de Año Nuevo",
        "year": 1800,  # año fuera de rango (debe fallar)
        "country": "US",
        "is_renounceable": False,
        "is_local": False,
        "start": datetime(2025, 1, 1, 0, 0).isoformat(),
        "end": datetime(2025, 1, 1, 23, 59).isoformat(),
        "enable": True
    }
    response = client.post("/feriados/", json=data)
    assert response.status_code == 422  # Debe fallar con un 422
    assert "year" in response.json()["detail"][0]["loc"]  # 📌 Verifica el campo con error


def test_invalid_country():
    Prueba que falla si el país no tiene 2 caracteres
    data = {
        "name": "Año Nuevo",
        "public_name": "Día de Año Nuevo",
        "year": 2025,
        "country": "USA",  # más de 2 caracteres (debe fallar)
        "is_renounceable": False,
        "is_local": False,
        "start": datetime(2025, 1, 1, 0, 0).isoformat(),
        "end": datetime(2025, 1, 1, 23, 59).isoformat(),
        "enable": True
    }
    response = client.post("/feriados/", json=data)
    assert response.status_code == 422  # Debe fallar con un 422
    assert "country" in response.json()["detail"][0]["loc"] """