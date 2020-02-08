"""#place bets
for player in players:
    player.bet();

#deal cards
for spot in spots:
    if(spot.bet > 0):
        shoe.dealCard(spot.hand);

shoe.dealCard(dealer.upCard);

for spot in spots:
    shoe.dealCard(player.hand);

shoe.dealCard(dealer.downCard);

#play player hands
for player in players:
    while(player.activeHands >= 1):
        decision = player.makeDecision():
        while(decision != "stand") and ()):
            if decision == "hit";

    
#play dealer hand

#pay bets



"""
import random

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
        self.bankRoll = 50000
        self.activeSpots = []
        self.desiredSpots = 1

    def ClearSpots(self):
        self.activeSpots = []
    
    def CalculateDesiredSpots(self):
        self.desiredSpots = 1
    
    def ClaimSpot(self, spot):
        self.activeSpots.append(spot)
        spot.activePlayer = self

    def CalculateBets(self, min, max):
        self.bet = min
    
    def Bet(self):
        self.PlaceBet(self.activeSpots[0])
        # for spot in self.activeSpots:
        #     self.PlaceBet(spot)

    def PlaceBet(self, spot):
        spot.PlaceBet(self.bet)
        self.bankRoll -= self.bet
    
    def PlaceAnotherBet(self, spot):
        spot.PlaceAnotherBet(self.bet)
        self.bankRoll -= self.bet




class InputPlayer(Player):
    def __init__(self):
        print("Enter Name: ")
        name = input()
        Player.__init__(self, name)
    
    def Decision(self, hand):
        print(self.name + " what would you like to do with ", end='')
        printHand(hand, '\n')
        return input()


class Spot:
    def __init__(self):
        self.activePlayer = None
        self.splits = 0
        self.hands = []
        self.basebet = 0 

    def PlaceNewBet(self, bet):
        self.bets.append(bet)
    

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        try:
            self.value = int(face)
        except:
            if(face == "A"):
                self.value = 1
            else:
                self.value = 10

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.soft = False
        self.busted = False
        self.split = False
    def DealCard(self, card):
        self.cards.append(card)
        self.UpdateValue()
    def RemoveTopCard(self):
        card = self.cards.pop()
        self.UpdateValue()
        return card
    def UpdateValue(self):
        self.value = 0
        for card in self.cards:
            self.value += card.value
            if((card.face == "A") and (self.value <= 11)):
                self.value += 10
                self.soft = True
        if((self.value > 21)  and (self.soft)):
            self.value -= 10
            self.soft = False
        self.busted = (self.value > 21)

class SplitHand(Hand):
        def __init__(self, card):
            Hand.__init__(self)
            self.DealCard(card)
            self.split = True

class DealerHand(Hand):
    def __init(self):
        self.upCard = None
        self.downCard = None
        Hand.__init__(self)
    
    def DealCard(self, card):
        Hand.DealCard(self, card)
        if(len(self.cards) == 1):
            self.upCard = self.cards[0]
        if(len(self.cards) == 2):
            self.downCard = self.cards[1]


deck = [Card("A", "spades"),
        Card("2", "spades"),
        Card("3", "spades"),
        Card("4", "spades"),
        Card("5", "spades"),
        Card("6", "spades"),
        Card("7", "spades"),
        Card("8", "spades"),
        Card("9", "spades"),
        Card("10", "spades"),
        Card("J", "spades"),
        Card("Q", "spades"),
        Card("K", "spades"),
        Card("A", "hearts"),
        Card("2", "hearts"),
        Card("3", "hearts"),
        Card("4", "hearts"),
        Card("5", "hearts"),
        Card("6", "hearts"),
        Card("7", "hearts"),
        Card("8", "hearts"),
        Card("9", "hearts"),
        Card("10", "hearts"),
        Card("J", "hearts"),
        Card("Q", "hearts"),
        Card("K", "hearts"),
        Card("A", "clubs"),
        Card("2", "clubs"),
        Card("3", "clubs"),
        Card("4", "clubs"),
        Card("5", "clubs"),
        Card("6", "clubs"),
        Card("7", "clubs"),
        Card("8", "clubs"),
        Card("9", "clubs"),
        Card("10","clubs"),
        Card("J", "clubs"),
        Card("Q", "clubs"),
        Card("K", "clubs"),
        Card("A", "diamonds"),
        Card("2", "diamonds"),
        Card("3", "diamonds"),
        Card("4", "diamonds"),
        Card("5", "diamonds"),
        Card("6", "diamonds"),
        Card("7", "diamonds"),
        Card("8", "diamonds"),
        Card("9", "diamonds"),
        Card("10", "diamonds"),
        Card("J", "diamonds"),
        Card("Q", "diamonds"),
        Card("K", "diamonds"),
        ]

class Shoe:
    def __init__(self, numDecks):
        self.cards = []
        self.cutCardPosition = 0
        for x in range(numDecks):
            self.cards.extend(deck)
        self.numDecksStart = numDecks
        self.numCardsStart = len(self.cards)
    
    def Shuffle(self):
        i = 0
        for card in self.cards:
            i += 1
            index = random.randint(0,len(self.cards)-1)
            temp = card
            card = self.cards[index]
            self.cards[index] = temp

    def TakeCard(self):
        return self.cards.pop()

    def DealCard(self, hand):
        card = self.cards.pop()
        hand.DealCard(card)
    
    def NumCards(self):
        return len(self.cards)

    def NumDecks(self):
        return float(self.NumCards())/len(deck)

    def PlaceCutCard(self, decks):
        self.cutCardPosition = decks*len(deck)

    def ReachedCutCard(self):
        return (self.NumCards() < self.cutCardPosition)

class Discard():
    def __init__(self):
        self.cards = []
    
    def TakeCards(self, cards):
        self.cards.extend(cards)
    
    def TakeHand(self, hand):
        self.cards.extend(hand.cards)
    
    def NumCards(self):
        return len(self.cards)

    def NumDecks(self):
        return float(self.NumCards())/len(deck)

class Table:
    def __init__(self, spots, chairs, rules):
        self.spots = []
        for x in range(spots):
            self.spots.append(Spot())
        self.chairs = []
        for x in range(chairs):
            self.chairs.append(Chair())
        self.rules = rules

class Chair:
    def __init__(self):
        self.activePlayer = None    

basicRules = {
    "minBet": 5,
    "maxBet": 100,
    "DAS": True,
    "RSA": True,
    "HitTilHard": 17,
    "HitTilSoft": 18,
    "MaxSplits": 4,
    "EarlySurrender": False,
    "LateSurrender": False,
    "BlackJackPays": float(3)/2,
    "Double": "Any"
}

inputPlayers = [
    InputPlayer(),
    InputPlayer(),
    InputPlayer(),
    InputPlayer(),
    InputPlayer(),
    InputPlayer()
]

seatingAssignments = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]

#set up table
table = Table(6, 6, basicRules)
discard = Discard()
shoe = Shoe(6)
shoe.Shuffle()
spots  = table.spots
dealerHand = DealerHand()

#set up players
players = inputPlayers

for player in players:
    player.ClearSpots()

for spot in spots:
    spot.activePlayer = None

for assignment in seatingAssignments:
    players[assignment[1]].ClaimSpot(players[assignment[1]])

for player in players:
    player.CalculateBets( table.rules["minBet"], table.rules["maxBet"] )
    player.Bet()

#deal first cards
for spot in spots:
    if(spot.bet >= table.rules["minBet"]):
        spot.hands.append(Hand())
        shoe.DealCard(spot.hands[0])

#deal dealer hand
shoe.DealCard(dealerHand)

#deal second cards
for spot in spots:
    for hand in spot.hands:
        shoe.DealCard(spot.hand)

#deal second dealer card
shoe.DealCard(dealerHand)

#print Hands
for spot in spots:
    print("Player " + spot.activePlayer.name + " Hand - ", end='')
    printHand(spot.hands[0], "\n")

print("Dealer upcard - ", end='')
print(dealerHand.upCard.face + ' ' + dealerHand.upCard.suit)

#resolve player actions
for spot in spots:
    currentHand = 0
    while(currentHand<len(spot.hands)):
    #for hand in spot.hands:
        hand = spot.hands[currentHand]
        while(1):
            while(len(hand.cards) < 2):
                shoe.DealCard(hand)

            if(hand.busted):
                discard.TakeHand(hand)
                spot.hands.remove(hand)
                break
            if(hand.value == 21):
                if(len(hand.cards) == 2 and not(hand.split)):
                    discard.TakeHand(hand)
                    spot.hands.remove(hand)
                    print("Player " + spot.activePlayer.name + " BlackJack")
                else:
                    print("Congrats 21")
                currentHand += 1
                break

            action = spot.activePlayer.Decision(hand)
            if(action == "stand"):
                currentHand += 1
                break
            elif(action == "hit"):
                shoe.DealCard(hand)
            elif(action == "double"):
                if(len(hand.cards) == 2):
                    shoe.DealCard(hand)
                    currentHand += 1
                    break
                else:
                    print("Cannot Double")
            elif(action == "split"):
                if(len(hand.cards) == 2) and (hand.cards[0].value == hand.cards[1].value) and (spot.splits < 4):
                    card = hand.RemoveTopCard()
                    spot.hands.append(SplitHand(card))
                    hand.split = True
                    spot.splits += 1
                    shoe.DealCard(hand)
                elif(spot.splits >= 4):
                    print("Max splits reached")
                else:
                    print("Cannot Split")
            elif(action == "surrender"):
                print("No support for surrender yet")
            else:
                print("Action not valid")

        printHand(hand, '\n')

#resolve dealer action
print("Dealer downcard - ", end='')
print(dealerHand.downCard.face + ' ' + dealerHand.downCard.suit)

while((dealerHand.value < 17 and dealerHand.soft == False) or (dealerHand.value < 18 and dealerHand.soft == True)):
    print("Dealer Hit", end=' ')
    printHand(dealerHand, '\n')
    shoe.DealCard(dealerHand)

print("Dealer Hand", end=' ')
printHand(dealerHand, '\n')

#resolve winners
for spot in reversed(spots):
    for hand in reversed(spot.hands):
        print(spot.activePlayer.name, end=' ')
        printHand(hand, '')
        if((dealerHand.value > 21) or (hand.value > dealerHand.value)):
            print(" wins!")
        elif(hand.value == dealerHand.value):
            print(" pushes!")
        else:
            print("loses")
        discard.TakeHand(hand)
        spot.hands.remove(hand)

discard.TakeHand(dealerHand)
dealerHand.cards.clear()
print(discard.NumCards())
for card in discard.cards:
    print(card.face, end=' ')

