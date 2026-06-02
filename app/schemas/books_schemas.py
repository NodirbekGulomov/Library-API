from pydantic import BaseModel


class BookCreate(BaseModel):
    nomi: str
    muallifi: str
    nashr_yili: int
    sahifalar_soni: int


class BookResponse(BaseModel):
    id: int
    nomi: str
    muallifi: str
    nashr_yili: int
    sahifalar_soni: int


class BookUpdate(BaseModel):
    nomi: str
    muallifi: str | None = None
    nashr_yili: int | None = None
    sahifalar_soni: int | None = None
