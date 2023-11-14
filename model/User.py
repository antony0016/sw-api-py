from model import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'user'
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=False)
