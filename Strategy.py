import csv
import os

class Strategy():
    def __init__(self, path, rules):
        os.chdir('C:\\PythonLearning\\BlackJackSim\\'+ path)
        with open('HardHands.csv', 'r') as f:
            reader = csv.reader(f)
            self.hardHands = list(reader)
        with open('HardHandsNoDouble.csv', 'r') as f:
            reader = csv.reader(f)
            self.hardHandsNoDouble = list(reader)
        with open('SoftHands.csv', 'r') as f:
            reader = csv.reader(f)
            self.softHands = list(reader)
        with open('SoftHandsNoDouble.csv', 'r') as f:
            reader = csv.reader(f)
            self.softHandsNoDouble = list(reader)
        with open('Splits.csv', 'r') as f:
            reader = csv.reader(f)
            self.splits = list(reader)
        self.rules = rules
    
    def Decision(self, hand, upCard):
        # print(self.hardHands)
        # print(self.hardHandsNoDouble)
        # print(self.softHands)
        # print(self.softHandsNoDouble)
        # print(self.splits)
        # print ("Entering Stategy decision")
        # print (" Hand value = " + str(hand.value))
        # print (" Hand is pair = " + str(hand.isPair()))
        if(hand.isPair()):
            if(hand.split < (self.rules["MaxSplits"] - 1) ):
                split = self.splits[(10-hand.cards[0].value)][upCard.value - 1]
                # print(split)
                split = int(split)
                # print(split)
                split = bool(split)
                # print(split)
                if(split):
                    # print ("returning split")
                    return "split"

        # print (" Hand soft = " + str(hand.soft))
        # print (" Hand canDouble = " + str(hand.canDouble()))
        if(hand.soft):
            if(hand.canDouble()):
                decision = self.softHands[(21-hand.value)][upCard.value-1]
            else:
                decision = self.softHandsNoDouble[(21-hand.value)][upCard.value-1]
        else:
            if(hand.canDouble()):
                decision = self.hardHands[(21-hand.value)][upCard.value-1]
            else:
                decision = self.hardHandsNoDouble[(21-hand.value)][upCard.value-1]
        
        # print("returning " + decision)
        return decision