from fastapi import FastAPI

from app.apis import books_api
from app.db import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(books_api.router)
