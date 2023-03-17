from fastapi import APIRouter
from .routes.produtos import router as produto_router
from .routes.users import router as user_router

router = APIRouter()
router.include_router(produto_router)
router.include_router(user_router)
