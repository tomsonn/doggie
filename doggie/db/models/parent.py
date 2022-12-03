from doggie.db.base_class import Base

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Parent(Base):
    __tablename__ = 'parents'

    id = Column(UUID, primary_key=True)
    self_id = Column(UUID, ForeignKey('dogs.id'), nullable=False)

    dog = relationship('Dog', back_populates='parent')
    litter = relationship('Litter', back_populates='parent')
