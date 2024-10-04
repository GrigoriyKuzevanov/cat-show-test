from fastapi.testclient import TestClient

from src.app.models import Breed
from src.app.schemas import schemas_breeds


def test_get_breeds(client: TestClient, test_breeds: list[Breed]) -> None:
    response = client.get("/breeds/")

    assert response.status_code == 200

    breeds = [schemas_breeds.BreedOut(**breed) for breed in response.json()]

    assert len(breeds) == len(test_breeds)

    for index, breed in enumerate(breeds):
        assert breed.name == test_breeds[index].name
        assert breed.id == test_breeds[index].id
