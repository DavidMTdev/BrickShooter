from models.player import Player
from config.base import session


class Auth:
    def __init__(self):
        pass

    def getSession(self):
        return self.session

    def register(self, pseudo, password):
        if ((pseudo and not pseudo.isspace()) and (password and not password.isspace())):
            player = Player(pseudo, 0, password, 0)

            session.add(player)
            session.commit()
            # session.close()
            p = Player.getPlayer(player.pseudo)
            return p

    def login(self, pseudo, password):
        players = Player.getAllPlayer()

        for player in players:
            if pseudo == player.pseudo and password == player.password:
                return player
