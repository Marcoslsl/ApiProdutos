from src.infra.db.repo import ProdutoRepo
from src.models import Produto
from fastapi import APIRouter, status

router = APIRouter()

@router.post("/produtos", status_code=status.HTTP_201_CREATED)
def register(produto: Produto):
    prod_repo = ProdutoRepo()
    prod = prod_repo.create(produto)
    return prod

@router.get("/produtos")
def list_all():
    prod_repo = ProdutoRepo()
    prod = prod_repo.list_all()
    return prod

@router.get("/produtos/{product_id}")
def get(product_id: int):
    prod_repo = ProdutoRepo()
    prod = prod_repo.get(product_id)
    return prod

@router.delete("/produtos/{product_id}")
def delete(product_id: int):
    prod_repo = ProdutoRepo()
    prod = prod_repo.remove(product_id)
    return prod
