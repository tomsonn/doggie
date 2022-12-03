from datetime import date

from pydantic import BaseModel


class Kennel(BaseModel):
    id: int
    origin_date: date
    name: str
    country: str
    club_id: int | None = None

    class Config:
        orm_mode = True
