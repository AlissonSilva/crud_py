from fastapi import Depends, HTTPException, APIRouter, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security.jwt_handler import get_current_user
from controller import categorycontroller
from controller.usercontroller import obter_usuario_por_username
from schemas.category_schema import CategoryCreate, CategoryResponse

auth_scheme = HTTPBearer()

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
def categorias(current_user: dict = Depends(get_current_user)):
    try:
        print(f"Usuário atual: {current_user}")  
        return categorycontroller.categorias()
    except Exception as e:
        print(f"Erro ao obter categorias: {e}")
        raise HTTPException(status_code=500, detail="Erro ao obter categorias")

@router.post("/")
def criar_categoria( categoria: CategoryCreate, current_user: dict = Depends(get_current_user) ):
    username = current_user.get("sub")
    usuario = obter_usuario_por_username(username)
    print("username: ",username)
    print("usuario:",usuario.id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    user_id = usuario.id
    nova_categoria = categorycontroller.criar_categoria(
        name=categoria.name,
        description=categoria.description,
        user_created=user_id
    )
    return nova_categoria   

@router.get("/{category_id}")
def obter_categoria_por_id(category_id: int, current_user: dict = Depends(get_current_user)):
    categoria = categorycontroller.obter_categoria_por_id(category_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.put("/{category_id}")
def atualizar_categoria(category_id: int, novo_nome: str | None = None, nova_descricao: str | None = None, current_user: dict = Depends(get_current_user)):
    categoria_atualizada = categorycontroller.atualizar_categoria(category_id, novo_nome, nova_descricao)
    if not categoria_atualizada:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
@router.delete("/{category_id}")
def deletar_categoria(category_id: int, current_user: dict = Depends(get_current_user)):
    username = current_user.get("sub")
    usuario = obter_usuario_por_username(username)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    user_id = usuario.id
    categoria_deletada = categorycontroller.deletar_categoria(category_id, user_deleted=user_id)
    if not categoria_deletada:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return {"detail": "Categoria deletada com sucesso"}