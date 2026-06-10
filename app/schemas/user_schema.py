from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    nombre: str
    email: str

    class config:
        from_attributes = True