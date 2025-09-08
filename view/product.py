import controller.productcontroller as product_controller
from fastapi import Depends, HTTPException,APIRouter, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security.jwt_handler import get_current_user

auth_scheme = HTTPBearer()

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def produtos(current_user: dict = Depends(get_current_user)):
    return product_controller.categorias()

@router.post("/")
def criar_produto(name: str, description: str, img: str, price: float, category_id: int, user_id: int, current_user: dict = Depends(get_current_user)):
    return product_controller.criar_produto(name, description, img, price, category_id, user_id)

@router.get("/{product_id}")
def obter_produto_por_id(product_id: int, current_user: dict = Depends(get_current_user)):
    produto = product_controller.obter_produto_por_id(product_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{product_id}")
def atualizar_produto(product_id: int, novo_nome: str | None = None, nova_descricao: str | None = None, novo_img: str | None = None, novo_price: float | None = None, novo_status: str | None = None, current_user: dict = Depends(get_current_user)):
    produto_atualizado = product_controller.atualizar_produto(product_id, novo_nome, nova_descricao, novo_img, novo_price, novo_status)
    if not produto_atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto_atualizado

@router.delete("/{product_id}")
def deletar_produto(product_id: int, current_user: dict = Depends(get_current_user)):
    produto_deletado = product_controller.deletar_produto(product_id, current_user['id'])
    if not produto_deletado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}