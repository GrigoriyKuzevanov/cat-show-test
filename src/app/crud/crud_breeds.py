from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Breed
from app.schemas import schemas_breeds


def read_all_breeds(session: Session, limit: int, skip: int) -> list:
    stmt = select(Breed).limit(limit).offset(skip)
    db_breeds = session.scalars(stmt).all()

    return db_breeds
