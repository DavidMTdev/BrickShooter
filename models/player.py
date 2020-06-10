from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from config.base import Base, Session


playerEquipment = Table(
    'player_equipment', Base.metadata,
    Column('player_id', Integer, ForeignKey('player.id')),
    Column('equipment_id', Integer, ForeignKey('equipment.id'))
)

session = Session()


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    pseudo = Column(String(50), nullable=True)
    credit = Column(Integer, nullable=True)
    password = Column(String(50), nullable=True)

    equipments = relationship("Equipment", secondary=playerEquipment, backref="players")

    saves = relationship('Save', backref='player')

    def __init__(self, pseudo, credit, password):
        self.pseudo = pseudo
        self.credit = credit
        self.password = password

    def getPlayer(id):
        return session.query(Player).filter_by(id=id).first()

    def getAllPlayer():
        return session.query(Player).all()
