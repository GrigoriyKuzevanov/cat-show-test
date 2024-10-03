from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import crud_breeds, crud_kittens
from app.schemas import schemas_kittens

kittens_router = APIRouter(prefix="/kittens", tags=["kittens"])


@kittens_router.get("/", response_model=list[schemas_kittens.KittenOut])
def get_kittens(limit: int = 10, skip: int = 0, session: Session = Depends(get_db)):
    return crud_kittens.read_all_kittens(session=session, limit=limit, skip=skip)


@kittens_router.get(
    "/by_breed/{breed_id}", response_model=list[schemas_kittens.KittenOut]
)
def get_kittens_by_breed(breed_id: int, session: Session = Depends(get_db)):
    return crud_kittens.read_kittens_by_breed_id(session=session, breed_id=breed_id)


@kittens_router.get("/{kitten_id}", response_model=schemas_kittens.KittenOut)
def get_kitten(kitten_id: int, session: Session = Depends(get_db)):
    db_kitten = crud_kittens.read_kitten_by_id(session=session, kitten_id=kitten_id)

    if not db_kitten:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Kitten with id: {kitten_id} does not exist",
        )

    return db_kitten


@kittens_router.post(
    "/", response_model=schemas_kittens.KittenOut, status_code=status.HTTP_201_CREATED
)
def post_kitten(
    kitten: schemas_kittens.KittenCreate, session: Session = Depends(get_db)
):
    db_breed = crud_breeds.read_breed_by_id(session=session, breed_id=kitten.breed_id)

    if not db_breed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Breed with id: {kitten.breed_id} does not exist",
        )

    return crud_kittens.create_kitten(session=session, kitten=kitten)


@kittens_router.put("/{kitten_id}", response_model=schemas_kittens.KittenOut)
def update_kitten(
    kitten_id: int,
    kitten: schemas_kittens.KittenUpdate,
    session: Session = Depends(get_db),
):
    db_kitten = crud_kittens.read_kitten_by_id(session=session, kitten_id=kitten_id)

    if not db_kitten:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Kitten with id: {kitten_id} does not exist",
        )

    db_breed = crud_breeds.read_breed_by_id(session=session, breed_id=kitten.breed_id)

    if not db_breed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Breed with id: {kitten.breed_id} does not exist",
        )

    return crud_kittens.update_kitten(
        session=session, update_data=kitten, db_kitten=db_kitten
    )


@kittens_router.delete("/{kitten_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_kitten(kitten_id: int, session: Session = Depends(get_db)):
    db_kitten = crud_kittens.read_kitten_by_id(session=session, kitten_id=kitten_id)

    if not db_kitten:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Kitten with id: {kitten_id} does not exist",
        )

    crud_kittens.delete_kitten(session=session, db_kitten=db_kitten)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
