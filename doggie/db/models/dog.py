from sqlalchemy import Column, Date, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from doggie.db.base_class import Base


class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(UUID, primary_key=True)
    kennel_id = Column(Integer, ForeignKey('kennels.id'), nullable=False)
    litter_id = Column(Integer, ForeignKey('litters.id'))
    name = Column(String, nullable=False)
    price_amount = Column(Float)
    price_currency = Column(String)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=False)

    kennel = relationship('Kennel', back_populates='dog')
    litter = relationship('Litter', back_populates='dog')
    parent = relationship('Parent', back_populates='dog')
