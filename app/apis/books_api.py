from fastapi import APIRouter

from app.schemas.books_schemas import BookCreate, BookResponse, BookUpdate
from app.services import book_service

router = APIRouter()


@router.post("/books", response_model=BookResponse)
def create_book(data: BookCreate):
    return book_service.create(data)


@router.get("/books", response_model=list[BookResponse])
def get_all_books():
    return book_service.get_all()


@router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    return book_service.get(book_id)


@router.patch("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, data: BookUpdate):
    return book_service.update(book_id, data)


@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    return book_service.delete(book_id)


@router.get("/search_books", response_model=list[BookResponse])
def search_books(muallif: str):
    return book_service.get_by_muallif(muallif)
