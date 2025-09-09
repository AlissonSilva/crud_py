from sqlalchemy.orm import sessionmaker
from model.category import Category
import util.util as db_util
import security.password_handler as pwd_handler

SessionLocal = db_util.SessionLocal

# CRUD
def categorias():
    with SessionLocal() as sessao:
        return sessao.query(Category).all()
    
def criar_categoria(name, description, user_created):
    with SessionLocal() as sessao:
        nova_categoria = Category(name=name, description=description, user_created=user_created)
        sessao.add(nova_categoria)
        sessao.commit()
        sessao.refresh(nova_categoria)
        return nova_categoria

def obter_categoria_por_id(category_id):
    with SessionLocal() as sessao:
        return sessao.query(Category).filter_by(id=category_id).first()
    
def atualizar_categoria(category_id, novo_nome=None, nova_descricao=None):
    with SessionLocal() as sessao:
        categoria = sessao.query(Category).filter_by(id=category_id).first()
        if categoria:
            if novo_nome:
                categoria.name = novo_nome
            if nova_descricao:
                categoria.description = nova_descricao
            sessao.commit()
        return categoria