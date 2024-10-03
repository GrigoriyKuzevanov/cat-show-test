from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import crud_kittens
from app.schemas import schemas_kittens

kittens_router = APIRouter(prefix="/kittens", tags=["kittens"])


@kittens_router.get("/", response_model=list[schemas_kittens.KittenOut])
def get_kittens(limit: int = 10, skip: int = 0, session: Session = Depends(get_db)):
    return crud_kittens.read_all_kittens(session=session, limit=limit, skip=skip)
