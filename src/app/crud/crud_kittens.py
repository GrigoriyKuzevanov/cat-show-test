from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Kitten
from app.schemas import schemas_kittens


def read_all_kittens(session: Session, limit: int, skip: int):
    stmt = select(Kitten).limit(limit).offset(skip)
    db_kittens = session.scalars(stmt).all()

    return db_kittens
