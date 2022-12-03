from uuid import UUID

from pydantic import BaseModel


class Parent(BaseModel):
    id: UUID
    self_id: UUID
