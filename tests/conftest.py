from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

from src.app.core.config import settings
from src.app.core.database import Base, get_db
from src.app.main import app
from src.app.models import Breed, Kitten

engine = create_engine(settings.testing_postgres_url.unicode_string())

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def session() -> Generator[Session, None, None]:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with TestingSessionLocal() as testing_session:
        yield testing_session


@pytest.fixture(scope="function")
def client(session: Session) -> Generator[TestClient, None, None]:
    def override_get_db():
        with session as s:
            yield s

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_breeds(session: Session) -> list[Breed]:
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

    stmt = select(Breed)
    db_breeds = session.scalars(stmt).all()

    return db_breeds


@pytest.fixture
def test_kittens(session: Session, test_breeds: list[Breed]) -> list[Kitten]:
    kittens_data = [
        {
            "name": "Poppy",
            "color": "red",
            "age_months": 4,
            "description": "A very nice kitten!",
            "breed_id": test_breeds[0].id,
        },
        {
            "name": "Misty",
            "color": "black",
            "age_months": 10,
            "description": "A little kitten",
            "breed_id": test_breeds[0].id,
        },
        {
            "name": "Gizmo",
            "color": "white",
            "age_months": 7,
            "description": "A cute tiny cat",
            "breed_id": test_breeds[1].id,
        },
    ]

    kittens_models = [Kitten(**kitten_data) for kitten_data in kittens_data]

    session.add_all(kittens_models)
    session.commit()

    stmt = select(Kitten)
    db_kittens = session.scalars(stmt).all()

    return db_kittens
