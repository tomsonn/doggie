from uuid import UUID

from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from doggie.db.base_class import Base


class Litter(Base):
    __tablename__ = 'litters'

    id = Column(Integer, primary_key=True, index=True)
    dogs_count = Column(Integer, nullable=False)
    order_letter = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    mother_id = Column(UUID, ForeignKey('parents.id'), nullable=False)
    father_id = Column(UUID, ForeignKey('parents.id'), nullable=False)
    kennel_id = Column(Integer, ForeignKey('kennels.id'), nullable=False)

    parent = relationship('Parent', back_populates='litter')
    kennel = relationship('Kennel', back_populates='kennel')
