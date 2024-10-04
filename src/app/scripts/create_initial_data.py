import logging

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.app.core.database import SessionLocal
from src.app.models import Breed, Kitten

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_breeds(session: Session) -> None:
    try:
        breeds_data = [
            {
                "name": "Bengal",
            },
            {
                "name": "Siamese",
            },
        ]

        breeds_models = [Breed(**breed_data) for breed_data in breeds_data]

        session.add_all(breeds_models)
        session.commit()

    except Exception as error:
        logger.error(f"Error while creating breeds: {error}")


def create_kittens(session: Session) -> None:
    try:
        stmt = select(Breed)
        breeds = session.scalars(stmt).all()
        
        kittens_data = [
            {
                # "id": 1,
                "name": "Poppy",
                "color": "red",
                "age_months": 4,
                "description": "A very nice kitten!",
                "breed_id": breeds[0].id,
            },
            {
                # "id": 2,
                "name": "Misty",
                "color": "black",
                "age_months": 10,
                "description": "A little kitten",
                "breed_id": breeds[0].id,
            },
            {
                # "id": 3,
                "name": "Gizmo",
                "color": "white",
                "age_months": 7,
                "description": "A cute tiny cat",
                "breed_id": breeds[1].id,
            },
        ]

        kittens_models = [Kitten(**kitten_data) for kitten_data in kittens_data]

        session.add_all(kittens_models)
        session.commit()

    except Exception as error:
        logger.error(f"Error while creating kittens: {error}")


if __name__ == "__main__":
    with SessionLocal() as session:
        create_breeds(session=session)
        create_kittens(session=session)
