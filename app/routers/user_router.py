from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_service.lista_users(db)


@router.post("/", response_model=list[UserResponse])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.crear_user(db, user)

