from fastapi import HTTPException
from sqlalchemy import select

from app.db.base import LocalSession
from app.db.models import Book
from app.schemas.books_schemas import BookCreate, BookUpdate


def create(data: BookCreate):
    with LocalSession() as session:
        book = Book(**data.model_dump())
        session.add(book)
        session.commit()
    return book


def get_all() -> list[Book]:
    with LocalSession() as session:
        return session.execute(select(Book)).scalars().all()


def get(book_id: int) -> Book:
    with LocalSession() as session:
        book = session.execute(
            select(Book).where(Book.id == book_id)
        ).scalar_one_or_none()

        if book is None:
            raise HTTPException(
                status_code=404, detail=f"Book with id[{book_id}] is not found!"
            )
        return book


def update(book_id: int, data: BookUpdate):
    with LocalSession() as session:
        book = session.execute(
            select(Book).where(Book.id == book_id)
        ).scalar_one_or_none()

        if data.nomi:
            book.nomi = data.nomi

        if data.muallifi:
            book.muallifi = data.muallifi

        if data.nashr_yili:
            book.nashr_yili = data.nashr_yili

        if data.sahifalar_soni:
            book.sahifalar_soni = data.sahifalar_soni

        session.commit()

        return book


def delete(book_id: int):
    with LocalSession() as session:
        book = session.execute(
            select(Book).where(Book.id == book_id)
        ).scalar_one_or_none()

        if book is None:
            raise HTTPException(
                status_code=404, detail=f"Book with id[{book_id}] is not found!"
            )
        session.delete(book)
        session.commit()


def get_by_muallif(muallif: str) -> list[Book]:
    with LocalSession() as session:
        return (
            session.execute(select(Book).where(Book.muallifi == muallif))
            .scalars()
            .all()
        )
