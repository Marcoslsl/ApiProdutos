from src.infra.db.repo import UserRepo
from src.models import User
from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
def register(user: User):
    user_repo = UserRepo()
    user_ = user_repo.create(user)
    return {"data": user_}


@router.get("/users")
def list_all():
    user_repo = UserRepo()
    user = user_repo.list_all()
    return {"data": user}
