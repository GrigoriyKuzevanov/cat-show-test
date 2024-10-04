import pytest
from fastapi.testclient import TestClient

from src.app.exceptions import BreedNotExistException, KittenNotExistException
from src.app.models import Breed, Kitten
from src.app.schemas import schemas_kittens


def test_get_kittens(client: TestClient, test_kittens: list[Kitten]) -> None:
    response = client.get("/kittens/")

    assert response.status_code == 200

    kittens = [schemas_kittens.KittenOut(**kitten) for kitten in response.json()]

    assert len(kittens) == len(test_kittens)

    for index, kitten in enumerate(kittens):
        assert kitten.name == test_kittens[index].name
        assert kitten.color == test_kittens[index].color
        assert kitten.age_months == test_kittens[index].age_months
        assert kitten.description == test_kittens[index].description
        assert kitten.breed_id == test_kittens[index].breed_id


def test_get_kittens_by_breed(
    client: TestClient, test_kittens: list[Kitten], test_breeds: list[Breed]
) -> None:
    breed_id = test_kittens[0].breed_id
    response = client.get(f"/kittens/by_breed/{breed_id}")

    assert response.status_code == 200

    kittens = [schemas_kittens.KittenOut(**kitten) for kitten in response.json()]

    assert len(kittens) == len(test_kittens) - 1

    for index, kitten in enumerate(kittens):
        assert kitten.name == test_kittens[index].name
        assert kitten.color == test_kittens[index].color
        assert kitten.age_months == test_kittens[index].age_months
        assert kitten.description == test_kittens[index].description
        assert kitten.breed_id == test_kittens[index].breed_id


@pytest.mark.parametrize("kitten_id", [1, 2, 3])
def test_get_kitten(
    client: TestClient, test_kittens: list[Kitten], kitten_id: int
) -> None:
    response = client.get(f"/kittens/{kitten_id}")

    assert response.status_code == 200

    kitten = schemas_kittens.KittenOut(**response.json())

    assert kitten.id == test_kittens[kitten_id - 1].id
    assert kitten.name == test_kittens[kitten_id - 1].name
    assert kitten.color == test_kittens[kitten_id - 1].color
    assert kitten.age_months == test_kittens[kitten_id - 1].age_months
    assert kitten.description == test_kittens[kitten_id - 1].description
    assert kitten.breed_id == test_kittens[kitten_id - 1].breed_id


@pytest.mark.parametrize("kitten_id", [1, 2, 3])
def test_get_kitten_not_exists(client: TestClient, kitten_id: int) -> None:
    response = client.get(f"/kittens/{kitten_id}")

    assert response.status_code == 404
    assert (
        response.json().get("detail")
        == KittenNotExistException(kitten_id=kitten_id).detail
    )


def test_post_kitten(client: TestClient, test_breeds: list[Breed]) -> None:
    kitten_data = {
        "name": "Poppy",
        "color": "red",
        "age_months": 4,
        "description": "A very nice kitten!",
        "breed_id": test_breeds[0].id,
    }

    response = client.post("/kittens/", json=kitten_data)

    assert response.status_code == 201

    kitten_to_post = schemas_kittens.KittenCreate(**kitten_data)
    created_kitten = schemas_kittens.KittenOut(**response.json())

    assert created_kitten.id == 1
    assert created_kitten.name == kitten_to_post.name
    assert created_kitten.color == kitten_to_post.color
    assert created_kitten.age_months == kitten_to_post.age_months
    assert created_kitten.description == kitten_to_post.description
    assert created_kitten.breed_id == kitten_to_post.breed_id


def test_post_kitten_with_breed_not_exist(client: TestClient) -> None:
    kitten_data = {
        "name": "Poppy",
        "color": "red",
        "age_months": 4,
        "description": "A very nice kitten!",
        "breed_id": 1,
    }

    response = client.post("/kittens/", json=kitten_data)

    assert response.status_code == 404
    assert (
        response.json().get("detail")
        == BreedNotExistException(breed_id=kitten_data["breed_id"]).detail
    )


def test_update_kitten(client: TestClient, test_kittens: list[Kitten]) -> None:
    kitten_id = test_kittens[0].id
    update_data = {
        "name": "Fluffy",
        "color": "grey",
        "age_months": 10,
        "description": "Still a very nice kitten!",
        "breed_id": 1,
    }

    response = client.put(f"/kittens/{kitten_id}", json=update_data)

    assert response.status_code == 200

    kitten_to_update = schemas_kittens.KittenUpdate(**update_data)
    updated_kitten = schemas_kittens.KittenOut(**response.json())

    assert updated_kitten.id == kitten_id
    assert updated_kitten.name == kitten_to_update.name
    assert updated_kitten.color == kitten_to_update.color
    assert updated_kitten.age_months == kitten_to_update.age_months
    assert updated_kitten.description == kitten_to_update.description
    assert updated_kitten.breed_id == kitten_to_update.breed_id
