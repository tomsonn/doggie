from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from doggie.db.base_class import Base


class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, nullable=False)

    kennel = relationship('Kennel', uselist=False, back_populates='club')
