
## Este script contiene los métodos que interactuan directamente con la base de datos
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import *

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user_data: UserCreate):
    new_user = User(
        nombre = user_data.nombre,
        email = user_data.email,
        password = user_data.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
