from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.player import playerEquipment
from config.base import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    price = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    avantage = Column(String(50), nullable=True)
    duration = Column(Integer, nullable=True)

    def __init__(self, name, price, value, avantage, duration):
        self.name = name
        self.price = price
        self.value = value
        self.avantage = avantage
        self.duration = duration
