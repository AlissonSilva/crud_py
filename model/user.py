from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from util.util import Base

# Modelo
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"




