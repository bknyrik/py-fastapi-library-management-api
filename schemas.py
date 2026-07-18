from datetime import date

from pydantic import BaseModel


class BookBaseModel(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class BookCreateModel(BookBaseModel):
    ...


class BookModel(BookBaseModel):
    id: int
