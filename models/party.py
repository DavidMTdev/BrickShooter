from sqlalchemy import Column, String, Integer, DateTime, PickleType
from sqlalchemy.orm import relationship
from datetime import datetime

from config.base import Base


class Party(Base):
    __tablename__ = 'party'

    id = Column(Integer, primary_key=True)
    plateau = Column(PickleType, nullable=True)
    name = Column(String(50), nullable=True)
    date = Column(DateTime, default=datetime.now(), nullable=True)
    array_asset = Column(PickleType)

    saves = relationship('Save', backref='party')

    def __init__(self, plateau, name, array_asset):
        self.plateau = plateau
        self.name = name
        self.array_asset = array_asset
