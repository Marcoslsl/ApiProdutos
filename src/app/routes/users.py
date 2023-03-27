from src.infra.db.repo import UserRepo
from src.models import User, UserNoPassword, Login
from fastapi import APIRouter, HTTPException
from typing import List
from src.infra.providers.has_provider import get_hash, verify_hash
from src.infra.providers.token_provider import *
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import JWTError

router = APIRouter()
ou2 = OAuth2PasswordBearer(tokenUrl="token")


def get_logged_user(token=Depends(ou2)):
    """Get logged user."""
    try:
        user_name = verify_access_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token.")

    if not user_name:
        raise HTTPException(status_code=401, detail="Invalid token.")

    user = UserRepo().get_by_name(user_name)

    return user


@router.get("/me")
def me(user: User = Depends(get_logged_user)):
    """Me."""
    return user


@router.post("/token")
def login(login: Login):
    """Login."""
    name = login.name
    senha = login.senha

    user = UserRepo().get_by_name(name=name)

    if len(user) == 0:
        raise HTTPException(
            status_code=400, detail=f"User '{name}' is not registered."
        )

    print(user[0].senha)

    senha_valida = verify_hash(senha, user[0].senha)

    if not senha_valida:
        raise HTTPException(
            status_code=400, detail=f"User '{name}' already registered."
        )

    token = create_access_token({"sub": name})
    return {"user": user, "access_token": token}


@router.post("/users")
def signup(user: User):
    """Register."""
    all_users = list_all()
    print(all_users)
    validation = any([user.name in user_.name for user_ in all_users])

    if validation:
        raise HTTPException(
            status_code=400, detail=f"User '{user.name}' already registered."
        )
    user.senha = get_hash(user.senha)
    user_repo = UserRepo()
    user_ = user_repo.create(user)
    return user_


@router.get("/users")  # , response_model=List[UserNoPassword])
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
