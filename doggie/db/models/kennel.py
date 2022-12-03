from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from doggie.db.base_class import Base


class Kennel(Base):
    __tablename__ = 'kennels'

    id = Column(Integer, primary_key=True, index=True)
    club_id = Column(Integer, ForeignKey('clubs.id'))
    origin_date = Column(Date, nullable=False)
    name = Column(String, nullable=False)

    club = relationship('Club', back_populates='kennel')
    dog = relationship('Dog', back_populates='kennel')
    litter = relationship('Litter', back_populates='kennel')
