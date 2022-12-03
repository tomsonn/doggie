from uuid import UUID
from datetime import date

from pydantic import BaseModel


class Litter(BaseModel):
    id: UUID
    dogs_count = int
    order_letter = str
    dob = date
    kennel_id = int
    mother_id = UUID
    father_id = UUID

    class Config:
        orm_mode = True