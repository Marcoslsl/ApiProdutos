from sqlalchemy.orm import Session
from src.infra.db.interfaces import RepoInterface
from src.infra.db.configs.database import SessionLocal
from src.models import User
from src.infra.db.models import User as UserTable


class UserRepo(RepoInterface):
    """User repository."""

    def __init__(self, db_conn: Session = SessionLocal()) -> None:
        """Construct."""
        self.db_conn = db_conn

    def create(self, user: User):
        """Register a user."""
        db_user = UserTable(name=user.name, phone=user.phone)
        self.db_conn.add(db_user)
        self.db_conn.commit()
        self.db_conn.refresh(db_user)
        self.db_conn.close()
        return db_user

    def list_all(self):
        """List all users."""
        users = self.db_conn.query(UserTable).all()
        return users

    def get(self):
        """Get a unique user by id."""
        pass

    def remove(self):
        """Remove a unique user by id."""
        pass
