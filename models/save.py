from sqlalchemy import Column, Integer, ForeignKey

from config.base import Base


class Save(Base):
    __tablename__ = 'save'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=True)
    party_id = Column(Integer, ForeignKey('party.id'), nullable=True)
    score_id = Column(Integer, ForeignKey('score.id'), nullable=True)

    def __init__(self, player, party, score):
        self.player_id = player.id
        self.party_id = party.id
        self.score_id = score.id
