import controller.usercontroller as user_controller
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users/")
def create_user(username: str, email: str, name: str):
    user = user_controller.criar_usuario(username, email, name)
    return user

@app.get("/users/")
def list_users():
    return user_controller.listar_usuarios()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = user_controller.obter_usuario_por_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user_email(user_id: int, new_email: str): 
    user = user_controller.atualizar_email(user_id, new_email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = user_controller.deletar_usuario(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}