#configuración de entorno en la base de datos para pruebas
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.database import get_db
from main import app
from src.models.holiday import Base

# base de datos en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# crear la base de datos antes de las pruebas
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)  # Crea las tablas en memoria
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)  # Elimina las tablas después de la prueba

# Cliente de pruebas
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
