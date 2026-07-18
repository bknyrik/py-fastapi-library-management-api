from typing import Generator

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import schemas
import models
import crud
from database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get(
    "/authors/",
    response_model=list[schemas.AuthorListRetrieveModel])
def get_all_authors(
    db: Session = Depends(get_db)
):
    return crud.get_author_list(db)


@app.get("/books/", response_model=list[schemas.BookModel])
def get_all_books(
    author_id: int | None = None,
    db: Session = Depends(get_db)
) -> list[models.Book]:
    return crud.get_book_list(db, author_id)


@app.post("/books/", response_model=schemas.BookModel)
def write_book(
    data: schemas.BookCreateModel,
    db: Session = Depends(get_db)
) -> models.Book:
    return crud.create_book(db=db, data=data)
