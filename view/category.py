import controller.categorycontroller as category_controller
from fastapi import Depends, HTTPException,APIRouter, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security.jwt_handler import get_current_user
from schemas.category_schema import CategoryCreate, CategoryResponse

auth_scheme = HTTPBearer()

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
def categorias(current_user: dict = Depends(get_current_user)):
    return category_controller.categorias()

@router.post("/", response_model=CategoryResponse)
def criar_categoria(cat : CategoryCreate, current_user: dict = Depends(get_current_user)):
    return category_controller.criar_categoria(name=cat.name, description=cat.description)   

@router.get("/{category_id}")
def obter_categoria_por_id(category_id: int, current_user: dict = Depends(get_current_user)):
    categoria = category_controller.obter_categoria_por_id(category_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.put("/{category_id}")
def atualizar_categoria(category_id: int, novo_nome: str | None = None, nova_descricao: str | None = None, current_user: dict = Depends(get_current_user)):
    categoria_atualizada = category_controller.atualizar_categoria(category_id, novo_nome, nova_descricao)
    if not categoria_atualizada:
        raise HTTPException(status_code=404, detail="Categoria não encontrada") 