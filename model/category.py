from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from util.util import Base

class Category(Base):
    __tablename__ = 'categories'    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    user_created = Column(Integer, ForeignKey('users.id'), nullable=False)
    deleted = Column(Float, default=False)
    deleted_at = Column(DateTime)
    user_deleted = Column(Integer, ForeignKey('users.id'), nullable=True)
    def __repr__(self):
        return f"<Category(name='{self.name}')>"