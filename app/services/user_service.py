from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.repositories   import user_repository


def lista_users(db:Session):
    return user_repository.get_all_users(db)

def crear_user(db: Session, user_data: UserCreate):
    return user_repository.create_user(db, user_data)