import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração do hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload if payload.get("exp") >= datetime.utcnow().timestamp() else None
    except jwt.PyJWTError:
        return None
    
def verificar_senha(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    
