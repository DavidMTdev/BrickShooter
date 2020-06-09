from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from config.base import Base


class Score(Base):
    __tablename__ = 'score'

    id = Column(Integer, primary_key=True)
    current_score = Column(Integer, nullable=True)
    max_score = Column(Integer, nullable=True)

    saves = relationship('Save', backref='score')

    def __init__(self, current_score, max_score):
        self.current_score = current_score
        self.max_score = max_score
