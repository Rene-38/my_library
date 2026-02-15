from sqlalchemy import select, delete
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

    @classmethod
    async def find_one(cls, id: int, session: AsyncSession):
        query = select(BookModel).where(BookModel.id == id)
        result = await session.execute(query)
        book_model = result.scalars().first()
        return book_model

    @classmethod
    async def update_book(cls, id: int, data: SBookAdd, session: AsyncSession):
        query = select(BookModel).where(BookModel.id == id)
        result = await session.execute(query)
        book_model = result.scalars().first()           #нашли нужную книгу по заданому id
        if book_model != None:
            book_model.title = data.title
            book_model.author = data.author
            book_model.year = data.year
            book_model.pages = data.pages
            await session.commit()
            await session.refresh(book_model)
            return book_model
        else:
            return None

    @classmethod
    async def dell(cls, id: int, session: AsyncSession):
        query = select(BookModel).where(BookModel.id == id)
        if query != None:
            stmt = delete(BookModel).where(BookModel.id == id)
            await session.execute(stmt)
            await session.commit()
        else:
            return None


