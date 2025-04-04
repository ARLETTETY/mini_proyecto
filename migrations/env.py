from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context
from src.config.database import engine  # Asegúrate de que esta es la conexión a la base de datos en tu proyecto

# Aquí importas tus modelos para que Alembic los reconozca
from src.models.combination_rule import CombinationRule
from src.models.combination_rule_r_schedule_deviation_rule import ReglasDeCombinacion
from src.models.schedule_deviation_rule import ScheduleDeviation

# Esta línea es la que configura Alembic para detectar las tablas y columnas a partir de los modelos
Base = declarative_base()

# Configuración de logging (para ver los logs de alembic)
fileConfig(context.config.config_file_name)

# Configuración de conexión
config = context.config
target_metadata = Base.metadata  # Aquí se obtiene la metadata de los modelos

def run_migrations_offline():
    """Ejecutar migraciones en modo offline (sin conexión a base de datos)"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata)
    
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecutar migraciones en modo online (con conexión a base de datos)"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        
        with context.begin_transaction():
            context.run_migrations()

# Elegir si correr migraciones en modo offline u online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
