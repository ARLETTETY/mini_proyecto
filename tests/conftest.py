import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from src.config.database import get_db, Base  # Importa Base antes de definir la base de datos
from src.models import * # Asegúrate de que Base esté definido en tu modelo
# Base de datos en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base de datos antes de las pruebas
@pytest.fixture(scope="function")
def db_session():
    """Configura la base de datos en memoria para cada prueba."""
    Base.metadata.create_all(bind=engine)  # Crea las tablas en memoria
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)  # Elimina las tablas después de la prueba

# Cliente de pruebas
@pytest.fixture(scope="function")
def client(db_session):
    """Crea un cliente de pruebas para FastAPI con una base de datos en memoria."""
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
