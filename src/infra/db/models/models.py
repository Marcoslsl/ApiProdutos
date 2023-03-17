from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.configs.database import Base


class Produto(Base):
    """Produto table."""

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    user_id = Column(Integer, ForeignKey("user.id", name="fk_usuario"))


class User(Base):
    """User table."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    senha = Column(String)
    phone = Column(String)
    produtos = relationship("Produto")
    pedido = relationship("Pedido")


class Pedido(Base):
    """Pedido table."""

    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    entrega = Column(String)
    endereco = Column(String)
    obs = Column(String)
    user_id = Column(Integer, ForeignKey("user.id", name="fk_usuario"))
    prod_id = Column(Integer, ForeignKey("produto.id", name="fk_produto"))
