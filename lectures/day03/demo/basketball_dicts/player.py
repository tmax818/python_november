
# TODO Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

from players import players

class Player:
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

kevin = Player(players[0])
jason = Player(players[1])