from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import crud_kittens
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
