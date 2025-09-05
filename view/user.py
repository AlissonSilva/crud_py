import controller.usercontroller as user_controller
from fastapi import Depends, HTTPException,APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(username: str, email: str, name: str, password: str):
    user = user_controller.criar_usuario(username, email, name, password)
    return user

@router.get("/")
def list_users():
    return user_controller.listar_usuarios()

@router.get("/{user_id}")
def read_user(user_id: int):
    user = user_controller.obter_usuario_por_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user_email(user_id: int, new_email: str): 
    user = user_controller.atualizar_email(user_id, new_email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    user = user_controller.deletar_usuario(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}