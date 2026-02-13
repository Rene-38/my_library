from fastapi import APIRouter
from typing import Annotated
from schemas.books import SBookAdd, SBook
from database import SessionDep
from repository import BookRepository

router = APIRouter(
        prefix="/books",
        tags=["Книги"]
)

@router.post("", response_model=SBook)
async def create_book(book: SBookAdd, session: SessionDep):
    book_model = await BookRepository.add_one(book, session)
    return book_model

@router.get("", response_model=list[SBook])
async def get_books(session: SessionDep):
    books = await BookRepository.find_all(session)
    return books

