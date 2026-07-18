from datetime import date

from pydantic import BaseModel


class AuthorBaseModel(BaseModel):
    name: str
    bio: str


class AuthorCreateModel(AuthorBaseModel):
    ...


class AuthorListRetrieveModel(AuthorBaseModel):
    id: int
    books: list[int]



class BookBaseModel(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class BookCreateModel(BookBaseModel):
    ...


class BookModel(BookBaseModel):
    id: int
