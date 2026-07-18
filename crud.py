from sqlalchemy.orm import Session

import models
import schemas


def get_author_by_id(db: Session, pk: int) -> models.Author | None:
    return db.query(models.Author).get(ident=pk)


def get_book_list(db: Session) -> list[models.Book]:
    return db.query(models.Book).all()


def create_book(db: Session, data: schemas.BookCreateModel) -> models.Book:
    book = models.Book(**data.model_dump())

    db.add(book)
    db.commit()
    db.refresh(book)

    return book
