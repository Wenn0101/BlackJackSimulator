

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.soft = False
        self.busted = False
        self.split = 0
    def DealCard(self, card):
        self.cards.append(card)
        self.UpdateValue()
    def RemoveTopCard(self):
        card = self.cards.pop()
        self.UpdateValue()
        return card
    def UpdateValue(self):
        self.value = 0
        self.soft = False
        for card in self.cards:
            self.value += card.value
            if((card.face == "A") and (self.value <= 11)):
                self.value += 10
                self.soft = True
        if((self.value > 21)  and (self.soft)):
            self.value -= 10
            self.soft = False
        self.busted = (self.value > 21)
    def isPair(self):
        return ( ((len(self.cards)) == 2) and (self.cards[0].value == self.cards[1].value) )
    def canDouble(self):
        return (len(self.cards) == 2)

    # def __del__(self):
    #     printHand(self, '')
    #     print(" deleted")

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

class SplitHand(Hand):
        def __init__(self, card, split):
            Hand.__init__(self)
            self.DealCard(card)
            self.split = split