# base de datos en memoria para pruebas 
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from src.config.database import get_db, Base
from src.models import *  

# Se usa solo un engine compartido en toda la vida de los tests
SQLALCHEMY_DATABASE_URL = "sqlite://"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crea una sesión vinculada al engine
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea las tablas solo una vez por sesión de test
@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Esto mantiene la sesión abierta durante la duración de cada test
@pytest.fixture(scope="function")
def db_session():
    """Crea una nueva sesión para cada test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

# Esto crea un cliente de pruebas para FastAPI
@pytest.fixture(scope="function")
def client(db_session):
    # Crea un cliente de pruebas para FastAPI con una base de datos en memoria
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
