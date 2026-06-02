from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)

    nomi: Mapped[str]
    muallifi: Mapped[str]
    nashr_yili: Mapped[int]
    sahifalar_soni: Mapped[int]
