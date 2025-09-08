from sqlalchemy.orm import sessionmaker
from model.product import Product
from model.category import Category
from model.user import User
import util.util as db_util
import security.password_handler as pwd_handler

SessionLocal = db_util.SessionLocal


def categorias():
    with SessionLocal() as sessao:
        return sessao.query(Product).innerjoin(Category).innerjoin(User).all()
    
def criar_produto(name, description, img, price, category_id, user_id):
    with SessionLocal() as sessao:
        novo_produto = Product(
            name=name, 
            description=description, 
            img=img, 
            price=price, 
            category_id=category_id, 
            user_id=user_id
        )
        sessao.add(novo_produto)
        sessao.commit()
        sessao.refresh(novo_produto)
        return novo_produto
    
def obter_produto_por_id(product_id):
    with SessionLocal() as sessao:
        return sessao.query(Product).innerjoin(Category).innerjoin(User).filter_by(id=product_id).first()
    
def atualizar_produto(product_id, novo_nome=None, nova_descricao=None, novo_img=None, novo_price=None, novo_status=None):
    with SessionLocal() as sessao:
        produto = sessao.query(Product).filter_by(id=product_id).first()
        if produto:
            if novo_nome:
                produto.name = novo_nome
            if nova_descricao:
                produto.description = nova_descricao
            if novo_img:
                produto.img = novo_img
            if novo_price is not None:
                produto.price = novo_price
            if novo_status:
                produto.product_status = novo_status
            sessao.commit()
        return produto
    
def deletar_produto(product_id, user_deleted):
    with SessionLocal() as sessao:
        produto = sessao.query(Product).filter_by(id=product_id).first()
        if produto:
            produto.deleted = True
            produto.deleted_at = db_util.datetime.utcnow()
            produto.user_deleted = user_deleted
            sessao.commit()
        return produto