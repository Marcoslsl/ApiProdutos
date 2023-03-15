from src.infra.db.repo import ProdutoRepo
from src.models import Produto
from fastapi import APIRouter, status

router = APIRouter()


@router.post("/produtos", status_code=status.HTTP_201_CREATED)
def register(produto: Produto):
    """Register."""
    prod_repo = ProdutoRepo()
    prod = prod_repo.create(produto)
    return prod


@router.get("/produtos")
def list_all():
    """List all."""
    prod_repo = ProdutoRepo()
    prod = prod_repo.list_all()
    return prod


@router.get("/produtos/{product_id}")
def get(product_id: int):
    """Get."""
    prod_repo = ProdutoRepo()
    prod = prod_repo.get(product_id)
    return prod


@router.delete("/produtos/{product_id}")
def delete(product_id: int):
    """Delete."""
    prod_repo = ProdutoRepo()
    prod = prod_repo.remove(product_id)
    return prod
