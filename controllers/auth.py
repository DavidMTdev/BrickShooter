from models.player import Player, playerEquipment
from models.equipment import Equipment
from models.save import Save
from config.base import session


class Auth:
    def __init__(self):
        self.session = None

    def getSession(self):
        return self.session

    def register(self, pseudo, password):
        player = Player(pseudo, 0, password)

        session.add(player)
        session.commit()
        session.close()

    def login(self, pseudo, password):
        players = Player.getAllPlayer()

        for player in players:
            if pseudo == player.pseudo and password == player.password:
                self.session = player
                return True

        return False
