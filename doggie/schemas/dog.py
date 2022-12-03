from datetime import date
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import Enum


class Gender(Enum):
    male = 'M'
    female = 'F'


class Currency(Enum):
    czech_crown = 'CZK'
    euro = 'EUR'
    british_pound_sterling = 'GBP'


class Breed(Enum):
    ast = 'ast'


class Dog(BaseModel):
    id: UUID
    name: str
    kennel_id: int | None
    litter_id: int | None
    price_amount: float | None
    price_currency: Currency | None
    gender: Gender
    dob = date
    breed = Breed

    class Config:
        orm_mode = True
