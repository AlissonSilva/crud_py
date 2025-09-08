from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from util.util import Base

class Category(Base):
    __tablename__ = 'categories'    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"<Category(name='{self.name}')>"