from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    img: str | None = None
    price: float
    product_status: str | None = "available"
    category_id: int
    user_id: int
    deleted: bool | None = False
    deleted_at: datetime | None = None
    user_deleted: int | None = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True