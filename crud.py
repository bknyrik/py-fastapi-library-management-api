from sqlalchemy.orm import Session

import models


def get_author_by_id(db: Session, pk: int) -> models.Author | None:
    return db.query(models.Author).get(ident=pk)
