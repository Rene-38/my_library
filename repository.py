from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.books import BookModel
from schemas.books import SBookAdd

class BookRepository:
    @classmethod
    async def add_one(cls, data: SBookAdd, session: AsyncSession) -> BookModel:
        book_dict = data.model_dump()
        book = BookModel(**book_dict)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    @classmethod
    async def find_all(cls, session: AsyncSession):
        query = select(BookModel)
        result = await session.execute(query)
        books_models = result.scalars().all()
        return books_models

