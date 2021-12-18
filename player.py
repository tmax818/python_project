class Player:

    def __init__(self, name, symbol="X"):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def win(self, game):
        self.wins += 1
