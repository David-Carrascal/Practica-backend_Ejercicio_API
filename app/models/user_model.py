## Importar tipos de datos (los que se asocian a las propiedades de los modelos)
from sqlalchemy import Column, Integer, String
## Se agrega este modelo a la Base inicial del Backend
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False,)