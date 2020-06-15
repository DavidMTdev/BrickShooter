from config.base import Engine, Base, Session

from models.party import Party
from models.player import Player, playerEquipment
from models.save import Save
from models.score import Score
from models.equipment import Equipment
from views.game import Game
# from models.equipmentPlayer import EquipmentPlayer

# 2 - generate database schema
Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)

# session = Session()

# player = Player("david", 20000, "aerty")
# player2 = Player("louis", 20000, "aerty")
# equipment = Equipment("name", 2, 3, 'avantage', 4)
# equipment2 = Equipment("name", 2, 3, 'avantage', 4)
# score = Score(10, 20)
# party = Party([[0, "zaezea"], [0, "zaezea"], [0, "zaezea"]], "name", [player, 0])
# save = Save(player, party, score)

# session.add(party)
# session.add(player)
# session.add(player2)
# session.add(equipment)
# session.add(equipment2)
# session.add(score)

# session.commit()

# player.equipments.append(equipment)
# player.equipments.append(equipment2)

# session.add(save)

# session.commit()

# p = session.query(Party).first()
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(player.getPlayer(2).pseudo)
# print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

# print(p.plateau)
# print(p.plateau[0])
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

# print(equipment)

# print(p.array_asset[0].pseudo)

# for player in equipment.players:
#     print("fzedhvguhjqsgfzdqfgsDGFJSDgfhjsDGFjsdhsDGFSgdjk")
#     print(player.pseudo)

# print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
# print(session.query(Equipment).filter(Equipment.players.any(id=1)).all())

# print(session.query(Player).filter(Player.equipments.any(id=1)).all())

# print(player.getAllPlayer())


# session.close()
