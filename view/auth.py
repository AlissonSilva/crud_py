from fastapi import APIRouter, HTTPException
from controller import authcontroller
from schemas.auth_schema import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(login_request: LoginRequest):
    token = authcontroller.autenticar_usuario(login_request)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token