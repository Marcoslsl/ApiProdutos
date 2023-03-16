from src.infra.db.repo import UserRepo
from src.models import User, UserNoPassword
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.post("/users")
def register(user: User):
    """Register."""
    user_repo = UserRepo()
    user_ = user_repo.create(user)
    return user_


@router.get("/users", response_model=List[UserNoPassword])
def list_all():
    """List all."""
    user_repo = UserRepo()
    user = user_repo.list_all()
    return user


@router.get("/users/{user_id}")
def get(user_id: int):
    """Get."""
    user_repo = UserRepo()
    user = user_repo.get(user_id)
    return user


@router.delete("/users/{user_id}")
def delete(user_id: int):
    """Delete."""
    user_repo = UserRepo()
    user = user_repo.remove(user_id)
    return user
