from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    description: str
    user_created: int | None = None
    created_at: str | None = None

class CategoryCreate(BaseModel):
    name: str
    description: str
    user_created: int | None = None

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True