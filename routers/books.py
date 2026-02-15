from fastapi import APIRouter, HTTPException, status
from typing import Annotated
from schemas.books import SBookAdd, SBook
from database import SessionDep
from repository import BookRepository

router = APIRouter(
        prefix="/books",
        tags=["Книги"]
)

@router.post("", response_model=SBook, status_code=status.HTTP_201_CREATED)
async def create_book(book: SBookAdd, session: SessionDep):
    book_model = await BookRepository.add_one(book, session)
    return book_model

@router.get("", response_model=list[SBook], status_code=status.HTTP_200_OK)
async def get_books(session: SessionDep):
    books = await BookRepository.find_all(session)
    return books

@router.get("/{id}", response_model=SBook)
async def get_book(id: int, session:SessionDep):
    book = await BookRepository.find_one(id, session)
    if book != None:
        return book
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Книга не найдена"
                )

@router.put("/{id}", response_model=SBook)
async def put_book(id: int, data: SBookAdd,  session:SessionDep):
    book = await BookRepository.update_book(id, data, session)
    if book != None:
        return book
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
                )

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, session:SessionDep):
    book = await BookRepository.dell(id, session)
    if book == None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
                )

