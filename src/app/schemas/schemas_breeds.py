from pydantic import BaseModel


class BreedBase(BaseModel):
    name: str


class BreedCreate(BreedBase):
    pass


class BreedOut(BreedBase):
    id: int

    class Config:
        from_attributes = True
