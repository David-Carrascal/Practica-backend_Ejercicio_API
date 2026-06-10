## Importaciones necesarias para creara base de datos con SQLAlchemy
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

## URL de conexión a la Base de datos en PostgreSQL
DATABASE_URL = "postgresql://postgres:64xt3r17@localhost:5432/cmm_sena"

## Crear variable para iniciar, un engine o motor, ejecutar la base de datos 
engine = create_engine(DATABASE_URL)

## Se crea la sesión única por cada petición al backend
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base= declarative_base()

## function: Esta función se encarga de crear la conexión a la base de datos por cada conexión recibida
## Son sesiones independientes
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



