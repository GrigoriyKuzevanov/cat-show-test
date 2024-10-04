from pydantic import BaseModel, PositiveInt


class KittenBase(BaseModel):
    name: str
    color: str
    age_months: PositiveInt
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
