from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Kitten
from app.schemas import schemas_kittens


def read_all_kittens(session: Session, limit: int, skip: int) -> list:
    stmt = select(Kitten).limit(limit).offset(skip)
    db_kittens = session.scalars(stmt).all()

    return db_kittens


def read_kittens_by_breed_id(session: Session, breed_id: int) -> list:
    stmt = select(Kitten).where(Kitten.breed_id == breed_id)
    db_kittens = session.scalars(stmt).all()

    return db_kittens


def read_kitten_by_id(session: Session, kitten_id: int) -> Kitten | None:
    return session.get(Kitten, kitten_id)
