from sqlalchemy.orm import sessionmaker
from datetime import datetime
from model.category import Category
from model.user import User
import util.util as db_util
import security.password_handler as pwd_handler

SessionLocal = db_util.SessionLocal

# CRUD
def categorias():
    with SessionLocal() as sessao:
        try:
            resultados = sessao.query(Category, User).outerjoin(User, Category.user_created == User.id).filter(Category.deleted == False).all()
            json_result = []
            for categoria, usuario in resultados:
                categoria_dict = {
                    "id": categoria.id,
                    "name": categoria.name,
                    "description": categoria.description,
                    "created_at": categoria.created_at,
                    "user_created": {
                        usuario.id,
                        usuario.username,
                        usuario.email
                    }
                }
                json_result.append(categoria_dict)

            print(f"Resultados das categorias: {json_result}")
            return json_result
        except Exception as e:
            print(f"Erro ao executar a query: {e}")
            return []
        
        
def criar_categoria(name, description, user_created):
    with SessionLocal() as sessao:
        try:
            nova_categoria = Category(name=name, description=description, user_created=user_created)
            sessao.add(nova_categoria)
            sessao.commit()
            sessao.refresh(nova_categoria)
            json_result = {
                "id": nova_categoria.id,
                "name": nova_categoria.name,
                "description": nova_categoria.description,
                "created_at": nova_categoria.created_at,
                "user_created": nova_categoria.user_created
            }   
            return json_result
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
            return None

def obter_categoria_por_id(category_id):
    with SessionLocal() as sessao:
          try:
              resultado = sessao.query(Category, User).outerjoin(User, Category.user_created == User.id).filter(Category.id==category_id).filter(Category.deleted == False).first()
              json_result = []
              for categoria, usuario in resultado:
                    categoria_dict = {
                        "id": categoria.id,
                        "name": categoria.name,
                        "description": categoria.description,
                        "created_at": categoria.created_at,
                        "user_created": {
                            usuario.id,
                            usuario.username,
                            usuario.email
                        }
                    }
                    json_result.append(categoria_dict)
                    print(f"Resultados das categorias: {json_result}")
                    return json_result
          except Exception as e:
            print(f"Erro ao executar a query: {e}")
            return []
            
    
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
    
def deletar_categoria(category_id, user_deleted):
    with SessionLocal() as sessao:
        categoria = sessao.query(Category).filter_by(id=category_id).first()
        if categoria:
            categoria.deleted = True
            categoria.user_deleted = user_deleted
            categoria.deleted_at = datetime.utcnow()
            sessao.commit()
        return categoria