from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from util.util import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    description = Column(String(255))
    img = Column(String(255))
    price = Column(Float, nullable=False)
    product_status = Column(String(50), default='available')
    created_at = Column(DateTime, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)
    user_deleted = Column(Integer, ForeignKey('users.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price})>"