from Strategy import *

def printHand(hand,printEnd):
    if(hand.soft):
        print("Soft ", end='')
    print(str(hand.value) + " - ", end= '')
    for card in hand.cards:
        print(card.face + "  ", end='')
    if(hand.busted):
        print("Busted ", end='')
    print(end=printEnd)


class Player:
    def __init__(self, name):
        self.name = name
        self.bankRoll = 500000
        self.activeSpots = []
        self.desiredSpots = 1
        self.totalBet = 0
        self.totalReturn = 0

    def ClearSpots(self):
        self.activeSpots = []
    
    def CalculateDesiredSpots(self):
        self.desiredSpots = 1
    
    def ClaimSpot(self, spot):
        self.activeSpots.append(spot)
        spot.activePlayer = self

    def CalculateBets(self, min, max):
        self.betAmount = min

    def PlaceBets(self):
        if(self.betAmount != 0 ):
            self.PlaceBetInSpot(self.activeSpots[0])
        
    def PlaceBetInSpot(self, spot):
        self.totalBet += self.betAmount
        bet = Bet(self.betAmount, self)
        spot.recieveNewBet(bet)
    
    def GiveNewBet(self, amount):
        self.totalBet += amount
        return Bet(amount, self)

    def IncreaseBet(self,  bet, amount):
        if (bet.owner != self):
            print("Error, player asked to increase bet that isn't theirs")
        else:
            self.totalBet += amount
            bet.amount += amount
            self.bankRoll -= amount
    
    def TakeBet(self, bet):
        if (bet.owner != self):
            print("Error, player asked to take bet that isn't theirs")
        else:
            self.totalReturn += bet.amount
            self.bankRoll += bet.amount
            bet.amount = 0
    
    def Return(self):
        return self.totalReturn/self.totalBet

class InputPlayer(Player):
    def __init__(self):
        print("Enter Name: ")
        name = input()
        Player.__init__(self, name)
    
    def Decision(self, hand, upCard):
        print( self.name + " what would you like to do with "+ str(hand.value) + " (", end='')
        printHand(hand, '') 
        print( ") vs Dealer " + upCard.face + ": ", end='' )
        return input()


class StrategyPlayer(Player):
    def __init__(self, strategy, rules):
        self.strategy = Strategy(strategy, rules)
        name = strategy + " Strategy Player"
        Player.__init__(self, name)

    def Decision(self, hand, upCard):
        decision = self.strategy.Decision(hand, upCard)
        # print( self.name + " Chose to "+ decision + " " + str(hand.value) + " (", end = '' )
        # printHand(hand, '') 
        # print( ") vs Dealer " + upCard.face )
        return decision

class BasicCountingPlayer(StrategyPlayer):
    def __init__(self, strategy, rules):
        self.estdecksRemaining = 6
        self.runningCount = 0
        StrategyPlayer.__init__(self, strategy, rules)
    
    def CalculateBets(self, min, max):
        self.betAmount = min
        if(self.TrueCount() < -2):
            self.betAmount = 0
        if(self.TrueCount() > 1.5):
            self.betAmount = min*2*round(self.TrueCount())
            if self.betAmount > max:
                self.betAmount = max
        #print(self.betAmount)
    
    def CalculateCount(self, discard):
        self.runningCount = 0
        for card in discard.cards:
            self.CountCard(card)

    def CountCard(self, card):
        if(card.value == 10 or card.value == 1):
            self.runningCount -= 1
        if( (card.value >= 2) and (card.value <= 6) ):
            self.runningCount += 1
    
    def updateShoeEstimate(self, shoe):
        self.estdecksRemaining = shoe.NumDecks()

    def TrueCount(self):
        return self.runningCount/self.estdecksRemaining

class Bet:
    def __init__(self, amount, owner):
        self.amount = amount
        self.owner = owner
        self.splits = 0
        self.hand = None
        owner.bankRoll -= amount