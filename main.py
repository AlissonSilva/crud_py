from fastapi import FastAPI
import view.user as user_view, view.auth as auth_view
import view.category as category_view
import view.product as product_view
from sqlalchemy import create_engine 
from util.util import Base, engine, SessionLocal
from model.user import User
import security.password_handler as pwd_handler


Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/", tags=["Root"])
def read_root():
    return {"Server": "Online"}


app.include_router(auth_view.router)
app.include_router(user_view.router)
app.include_router(category_view.router)
app.include_router(product_view.router)

def criar_usuario_padrao():
    with SessionLocal() as sessao:
        usuario = sessao.query(User).filter_by(username="admin").first()
        if not usuario:
            usuario = User(
                username="admin",
                name="Administrador",
                email="admin@admin.com",
                password=pwd_handler.hash_password("admin123")
            )
            sessao.add(usuario)
            sessao.commit()
            print("Usuário padrão criado: admin / admin123")

criar_usuario_padrao()