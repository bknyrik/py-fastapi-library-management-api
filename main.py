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


@app.get("/books/", response_model=list[schemas.BookModel])
def get_all_books(db: Session = Depends(get_db)) -> list[models.Book]:
    return crud.get_book_list(db)


@app.post("/books/", response_model=schemas.BookModel)
def write_book(
    data: schemas.BookCreateModel,
    db: Session = Depends(get_db)
) -> models.Book:
    return crud.create_book(db=db, data=data)
