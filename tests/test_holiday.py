import json
import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from main import app

# Prueba de creación de un feriado
def test_create_feriado(client: TestClient, db_session):
    
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

    response = client.post("/api/holiday/", json=data)  
    assert response.status_code == 201  
    assert response.json()["name"] == "Año Nuevo"

# Prueba de obtención de feriados
def test_get_feriados(client: TestClient, db_session):
   
    # crea un feriado para la prueba
    test_create_feriado(client, db_session)

    response = client.get("/api/holiday/")  
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

# Falla si el nombre es demasiado corto 
def test_invalid_name(client: TestClient):
    
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
    response = client.post("/api/holiday/", json=data)  
    assert response.status_code == 422  
    assert "name" in response.json()["detail"][0]["loc"]  

# Falla si el año no está en el rango válido
def test_invalid_year(client: TestClient):
    
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
    response = client.post("/api/holiday/", json=data)  
    assert response.status_code == 422  
    assert "year" in response.json()["detail"][0]["loc"]  

# Falla si el país no tiene 2 caracteres
def test_invalid_country(client: TestClient):
   
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
    response = client.post("/api/holiday/", json=data)  
    assert response.status_code == 422 
    assert "country" in response.json()["detail"][0]["loc"]  
