from config.base import session
from models.party import Party
from models.save import Save


class Part:
    def __init__(self):
        pass

    def createParty(self, name):

        if name and not name.isspace():

            party = Party([0, 0, 0, 0], name, [2, 'atout'])

            session.add(party)
            session.commit()
            session.close()

            return party
