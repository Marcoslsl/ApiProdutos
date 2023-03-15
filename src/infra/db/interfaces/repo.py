from abc import ABC, abstractmethod
from src.infra.db.configs.database import SessionLocal
from sqlalchemy.orm import Session


class RepoInterface(ABC):
    """Interface reposutory."""

    def __init__(self, db_conn: Session = SessionLocal()) -> None:
        """Construct."""
        self.db_conn = db_conn

    @abstractmethod
    def create(self):
        """Must implement."""
        raise NotImplementedError("Must be implemented.")

    @abstractmethod
    def list_all(self):
        """Must implement."""
        raise NotImplementedError("Must be implemented.")

    @abstractmethod
    def remove(self):
        """Must implement."""
        raise NotImplementedError("Must be implemented.")
