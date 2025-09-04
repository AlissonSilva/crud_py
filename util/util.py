import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco
Base = declarative_base()
engine = create_engine('sqlite:///dados.db', echo=True)
SessionLocal = sessionmaker(bind=engine)
# Criar tabelas
Base.metadata.create_all(engine)
