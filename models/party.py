from sqlalchemy import Column, String, Integer, DateTime, PickleType, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from config.base import Base


class Party(Base):
    __tablename__ = 'party'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    # name = Column(String(50), nullable=True)
    # date = Column(DateTime, default=datetime.now(), nullable=True)
    # array_asset = Column(PickleType)
    # player_id = Column(Integer, ForeignKey('player.id'), nullable=False)

    # saves = relationship('Save', backref='party')

    def __init__(self, score):
        self.score = score
        # self.name = name
        # self.array_asset = array_asset
