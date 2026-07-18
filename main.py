from typing import Generator

from fastapi import FastAPI

from database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


app = FastAPI()
