from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.app.core.database import get_db
from src.app.crud import crud_breeds
from src.app.schemas import schemas_breeds

breeds_router = APIRouter(prefix="/breeds", tags=["breeds"])


@breeds_router.get("/", response_model=list[schemas_breeds.BreedOut])
def get_breeds(limit: int = 10, skip: int = 0, session: Session = Depends(get_db)):
    return crud_breeds.read_all_breeds(session=session, limit=limit, skip=skip)
