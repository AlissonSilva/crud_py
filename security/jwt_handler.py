import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração do hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # ajuste o caminho se necessário

def criar_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verificar_token(token: str):
    print(f"Verificando token: {token}")  # Log do token recebido

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Payload decodificado: {payload}")  # Log do payload decodificado
        print(f"Expiração do token: {payload.get('exp')}")  # Log da expiração
        print(f"Hora atual: {datetime.utcnow().timestamp()}")  # Log da hora atual
        return payload
    except jwt.ExpiredSignatureError:
        print("Token expirado")
        return None
    except jwt.InvalidTokenError:
        print("Token inválido")
        return None
    except jwt.PyJWTError as e:
        print(f"Erro ao decodificar JWT: {e}")
        return None
    
def verificar_senha(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    print(f"Payload obtido em get_current_user: {payload}")  # Log do payload obtido
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

