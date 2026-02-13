from sqlalchemy.orm import Mapped, mapped_column
from database import Model

class BookModel(Model):
    __tablename__ = "library.db"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)   #init=False явно запрещает инициализация ID в конструкторе (для MappedAsDataclass).
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int | None]
    pages: Mapped[int | None]
    is_read: Mapped[bool] = mapped_column(default=False)

