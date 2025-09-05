from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: str
    name: str
    password: str  # já pensando no hash

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    name: str

    class Config:
        orm_mode = True  # permite retornar objetos do SQLAlchemy
