from sqlalchemy.orm import sessionmaker
from model.user import User
import util.util as db_util

SessionLocal = db_util.SessionLocal

# CRUD
def criar_usuario(username, email, name):
    with SessionLocal() as sessao:
        novo_usuario = User(username=username, email=email, name=name)
        sessao.add(novo_usuario)
        sessao.commit()
        sessao.refresh(novo_usuario)
        return novo_usuario

def obter_usuario_por_id(user_id):
    with SessionLocal() as sessao:
        return sessao.query(User).filter_by(id=user_id).first()

def atualizar_email(user_id, novo_email):
    with SessionLocal() as sessao:
        usuario = sessao.query(User).filter_by(id=user_id).first()
        if usuario:
            usuario.email = novo_email
            sessao.commit()
        return usuario

def deletar_usuario(user_id):
    with SessionLocal() as sessao:
        usuario = sessao.query(User).filter_by(id=user_id).first()
        if usuario:
            sessao.delete(usuario)
            sessao.commit()
        return usuario

def listar_usuarios():
    with SessionLocal() as sessao:
        return sessao.query(User).all()