import controller.usercontroller as user_controller
from fastapi import Depends, HTTPException,APIRouter, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security.jwt_handler import get_current_user
from schemas.user_schema import UserCreate, UserResponse

auth_scheme = HTTPBearer()

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/usuarios-protegidos")
def usuarios_protegidos(current_user: dict = Depends(get_current_user)):
    return {"msg": "Você está autenticado!", "user": current_user}

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, current_user: dict = Depends(get_current_user)):
    user = user_controller.criar_usuario(user.username, user.email, user.name, user.password)
    return user

@router.get("/")
def list_users(current_user: dict = Depends(get_current_user)):
    return user_controller.listar_usuarios()

@router.get("/{user_id}")
def read_user(user_id: int, current_user: dict = Depends(get_current_user)):
    user = user_controller.obter_usuario_por_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user_email(user_id: int, new_email: str, current_user: dict = Depends(get_current_user)): 
    user = user_controller.atualizar_email(user_id, new_email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, current_user: dict = Depends(get_current_user)):
    user = user_controller.deletar_usuario(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}