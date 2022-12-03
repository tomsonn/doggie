from pydantic import BaseModel


class Club(BaseModel):
    id: int
    country: str

    class Config:
        orm_mode = True
