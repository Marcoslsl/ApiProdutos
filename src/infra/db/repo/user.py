from sqlalchemy.orm import Session
from src.infra.db.interfaces import RepoInterface
from src.infra.db.configs.database import SessionLocal
from src.models import User
from src.infra.db.models import User as UserTable
from sqlalchemy import select, delete, update


class UserRepo(RepoInterface):
    """User repository."""

    def __init__(self, db_conn: Session = SessionLocal()) -> None:
        """Construct."""
        self.db_conn = db_conn

    def create(self, user: User):
        """Register a user."""
        db_user = UserTable(name=user.name, phone=user.phone, senha=user.senha)
        self.db_conn.add(db_user)
        self.db_conn.commit()
        self.db_conn.refresh(db_user)
        self.db_conn.close()
        return db_user

    def list_all(self):
        """List all users."""
        users = self.db_conn.query(UserTable).all()
        users_ = []
        for user in users:
            print(user.senha)
            user_ = User(
                id=user.id, name=user.name, phone=user.phone, senha=user.senha
            )
            users_.append(user_)

        return users_

    def get(self, user_id: int):
        """Get a unique user by id."""
        stmt = select(UserTable).filter_by(id=user_id)
        serie = self.db_conn.execute(stmt).scalars().all()

        return serie

    def remove(self, user_id: int):
        """Remove a unique user by id."""
        stmt = delete(UserTable).where(UserTable.id == user_id)
        self.db_conn.execute(stmt)

        return None

    def update(self, user: User):
        """Update a unique register."""
        stmt = (
            update(UserTable)
            .where(UserTable.id == user.id)
            .values(
                name=user.name,
                details=user.details,
                price=user.price,
                available=user.available,
            )
        )
        self.db_conn.execute(stmt)

        users = self.get(user.id)

        return users
