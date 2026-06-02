from fastapi import APIRouter

from app.schemas.books_schemas import BookCreate, BookResponse, BookUpdate
from app.services import book_services

router = APIRouter()


@router.post("/books", response_model=BookResponse)
def create_book(data: BookCreate):
    return book_services.create(data)


@router.get("books", response_model=list[BookResponse])
def get_all_books():
    return book_services.get_all()


@router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    return book_services.get(book_id)


@router.patch("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, data: BookUpdate):
    return book_services.update(book_id, data)


@router.delete("/books/{book_id}", response_model=BookResponse)
def delete_book(book_id: int):
    return book_services.delete(book_id)


@router.get("/books", response_model=BookResponse)
def search_books(muallif: str):
    return book_services.get_by_muallif(muallif)
