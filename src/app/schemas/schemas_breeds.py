from pydantic import BaseModel


class BreedBase(BaseModel):
    id: int
    name: str


class BreedCreate(BreedBase):
    pass


class BreedOut(BreedBase):
    pass
