from pydantic import BaseModel
from typing import Optional, Type, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str

    
class Produto(BaseModel):
    id: Optional[str] = None
    # user: Type[User]
    name: str
    details: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    user: Type[User]
    produto: Type[Produto]
    quantidade: int
    entrega: bool = True
    endereco: str
    obs: Optional[str] = None
