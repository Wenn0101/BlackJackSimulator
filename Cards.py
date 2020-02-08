import random

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
            while(i<len(self.cards)):
                randomIndex = random.randint(i,len(self.cards)-1)
                temp = self.cards[randomIndex]
                self.cards[randomIndex] = self.cards[i]
                self.cards[i] = temp
                i += 1

    def receiveCards(self, cards):
        self.cards.extend(cards)

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