from pydantic import BaseModel


class KittenBase(BaseModel):
    name: str
    color: str
    age_months: int
    description: str
    breed_id: int


class KittenCreate(KittenBase):
    pass


class KittenUpdate(KittenBase):
    pass


class KittenOut(KittenBase):
    id: int

    class Config:
        from_attributes = True
