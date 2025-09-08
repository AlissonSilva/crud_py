from schemas.auth_schema import LoginRequest, TokenResponse
from util.util import SessionLocal
from model.user import User
import security.jwt_handler as jwt_handler
import security.password_handler as pwd_handler


def autenticar_usuario(login_request: LoginRequest):
    with SessionLocal() as sessao:
        user = sessao.query(User).filter_by(username=login_request.username).first()
        
        if user and pwd_handler.verify_password(login_request.password, user.password):
            token = jwt_handler.criar_token({"sub": user.username})
            return {"name":user.name,"username":user.username, "email":user.email,"access_token": token, "token_type": "bearer"}
        return None
    
def validar_token(token: str):
    return jwt_handler.verificar_token(token)   
