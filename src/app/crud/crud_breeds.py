from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Breed


def read_all_breeds(session: Session, limit: int, skip: int) -> list:
    stmt = select(Breed).limit(limit).offset(skip)
    db_breeds = session.scalars(stmt).all()

    return db_breeds


def read_breed_by_id(session: Session, breed_id: int) -> Breed | None:
    return session.get(Breed, breed_id)
