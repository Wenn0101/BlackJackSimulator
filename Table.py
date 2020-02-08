from Rules import *

class Spot:
    def __init__(self):
        self.activePlayer = None
        self.bet = None
    
    def recieveNewBet(self, bet):
        self.bet = bet
    
    def ClearBet(self):
        self.bet = None

class Table:
    def __init__(self, spots, chairs, rules):
        self.spots = []
        for x in range(spots):
            self.spots.append(Spot())
        # self.chairs = []
        # for x in range(chairs):
        #     self.chairs.append(Chair())
        self.rules = rules