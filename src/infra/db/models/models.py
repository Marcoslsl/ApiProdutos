from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.db.configs.database import Base


class Produto(Base):
    """Produto table."""

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)


class User(Base):
    """User table."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
