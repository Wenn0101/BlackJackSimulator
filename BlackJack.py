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

from Player import *
from Cards import *
from Hand import *
from Table import *
from Rules import *
import datetime


# def printHand(hand,printEnd):
#     if(hand.soft):
#         print("Soft ", end='')
#     print(str(hand.value) + " - ", end= '')
#     for card in hand.cards:
#         print(card.face + "  ", end='')
#     if(hand.busted):
#         print("Busted ", end='')
#     print(end=printEnd)

inputPlayers = [
    BasicCountingPlayer("BasicStrategy", basicRules),
    StrategyPlayer("BasicStrategy", basicRules),
    StrategyPlayer("BasicStrategy", basicRules),
    StrategyPlayer("BasicStrategy", basicRules),
    StrategyPlayer("BasicStrategy", basicRules),
    StrategyPlayer("BasicStrategy", basicRules)
]

seatingAssignments = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]

#set up table
startTime = datetime.datetime.now()
table = Table(6, 6, basicRules)
spots  = table.spots

discard = Discard()
shoe = Shoe(6)

#set up players
players = inputPlayers

for assignment in seatingAssignments:
    players[assignment[0]].ClaimSpot(spots[assignment[1]])

handsPlayed = 0
handsToPlay = 100000
while(handsPlayed < handsToPlay):
    discard = Discard()
    shoe = Shoe(6)
    # print( "Cards in shoe" + str(len(shoe.cards)) )
    # print( "Cards in discard" + str(len(discard.cards)) )
    shoe.Shuffle()
    shoe.PlaceCutCard(.75)

    while(shoe.NumCards() > shoe.cutCardPosition):
        dealerHand = DealerHand()
        betsOnTable = []
        for player in players:
            # print(player.name + ' Bankroll  = ' + str(player.bankRoll))
            player.CalculateBets( table.rules["minBet"], table.rules["maxBet"] )
            player.PlaceBets()

        #deal first cards

        for spot in spots:
            if(spot.bet):
                betsOnTable.append(spot.bet)

        for bet in betsOnTable:       
            if(bet.amount >= table.rules["minBet"]):
                bet.hand = Hand()
                shoe.DealCard(bet.hand)

        #deal dealer hand
        shoe.DealCard(dealerHand)

        #deal second cards
        for bet in betsOnTable:  
                shoe.DealCard(bet.hand)

        #deal second dealer card
        shoe.DealCard(dealerHand)

        #print Hands
        # for bet in betsOnTable:  
            # print("Player " + bet.owner.name + " Hand - ", end='')
            # printHand(bet.hand, "\n")

        # print("Dealer upcard - ", end='')
        # print(dealerHand.upCard.face + ' ' + dealerHand.upCard.suit)

        #if(dealer.upCard.face = "A"):
            #do insurance
        if(dealerHand.value != 21):
            #resolve player actions
            currentBet = 0
            while(currentBet<len(betsOnTable)):
                bet = betsOnTable[currentBet]
                hand = betsOnTable[currentBet].hand
                invalidActions = 0
                while(1):
                    while(len(hand.cards) < 2):
                        shoe.DealCard(hand)

                    if(hand.busted):
                        discard.TakeHand(hand)
                        del bet.hand
                        betsOnTable.remove(bet)
                        break
                    if(hand.value == 21):
                        if(len(hand.cards) == 2 and not(hand.split)):
                            discard.TakeHand(hand)
                            del bet.hand
                            bet.amount += bet.amount*table.rules["BlackJackPays"]
                            bet.owner.TakeBet(bet)
                            betsOnTable.remove(bet)
                            # print("Player " + bet.owner.name + " BlackJack")
                        else:
                            # print("Congrats 21")
                            currentBet += 1
                        break
                    if(( hand.split > 0) and (hand.cards[0].face == 'A') ):
                        currentBet += 1
                        break

                    action = bet.owner.Decision(hand, dealerHand.upCard)
                    if(action == "stand"):
                        currentBet += 1
                        break
                    elif(action == "hit"):
                        shoe.DealCard(hand)
                    elif(action == "double"):
                        if(len(hand.cards) == 2):
                            shoe.DealCard(hand)
                            bet.owner.IncreaseBet(bet, bet.amount)
                            currentBet += 1
                            break
                        # else:
                            # print("Cannot Double")
                    elif(action == "split"):
                        if( (hand.isPair()) and (bet.splits < 3) ):
                            card = hand.RemoveTopCard()
                            hand.split += 1
                            bet.splits += 1
                            betsOnTable.insert( currentBet+1, bet.owner.GiveNewBet(bet.amount,) )
                            betsOnTable[currentBet+1].hand = SplitHand(card, hand.split)
                            shoe.DealCard(hand)
                            if (hand.cards[0].face == 'A'):
                                currentBet += 1
                                break
                        # elif(bet.splits >= 4):
                            # print("Max splits reached")
                        # else:
                            # print("Cannot Split")
                    elif(action == "surrender"):
                        print("No support for surrender yet")
                    else:
                        print("Action not valid" + str(action))
                        invalidActions += 1
                        if invalidActions > 5:
                            print("Too many invalid actions, quitting")
                            currentBet += 1
                            break

                # printHand(hand, '\n')

        #resolve dealer action
        # print("Dealer downcard - ", end='')
        # print(dealerHand.downCard.face + ' ' + dealerHand.downCard.suit)

        while((dealerHand.value < 17 and dealerHand.soft == False) or (dealerHand.value < 18 and dealerHand.soft == True)):
            # print("Dealer Hit", end=' ')
            # printHand(dealerHand, '\n')
            shoe.DealCard(dealerHand)

        # print("Dealer Hand", end=' ')
        # printHand(dealerHand, '\n')

        #resolve winners
        for bet in reversed(betsOnTable):
            hand = bet.hand
            # print(bet.owner.name, end=' ')
            # printHand(hand, '')
            if((dealerHand.value > 21) or (hand.value > dealerHand.value)):
                bet.amount += bet.amount
                # print(" wins!")
            elif(hand.value == dealerHand.value):
                pass
                # print(" pushes!")
            else:
                bet.amount -= bet.amount
                # print("loses")
            discard.TakeHand(hand)
            del bet.hand

        discard.TakeHand(dealerHand)
        dealerHand.cards.clear()

        # print(discard.NumCards())
        # for card in discard.cards:
            # print(card.face, end=' ')

        while(len(betsOnTable) > 0):
            bet = betsOnTable.pop()
            bet.owner.TakeBet(bet)
        
        for spot in spots:
            spot.ClearBet()

        players[0].CalculateCount(discard)
        players[0].updateShoeEstimate(shoe)
            
        handsPlayed += 1
        # print("handsPlayed = " + str(handsPlayed))
        if(handsPlayed % (handsToPlay/100) == 0):
            print(str(100*handsPlayed/handsToPlay) + r"% done")

    # print("Cut card reached")
    # for player in players:
        # print(player.name + ' Bankroll  = ' + str(player.bankRoll))

    del shoe
    del discard

endTime = datetime.datetime.now()

timeDiff = endTime - startTime 
print("Simulation Time - " + str(timeDiff))

for player in players:
    print(player.name + ' Bankroll  = ' + str(player.bankRoll))

totalBankRoll = 0
for player in players:
    totalBankRoll += player.bankRoll

totalProfit = totalBankRoll - (3000000)
profitPerHand = totalProfit/(handsPlayed*len(players))
profitPerDollar = profitPerHand/5
print("Total change in bankroll of " + str(totalProfit) + " over " + str(handsPlayed) + " hands")
print(str(profitPerHand) + ' profit per hand')
print(str(profitPerDollar) + ' profit per dollar if all bet minimum')

for player in players:
    print("Player " + str(player.name) + " return " + str(player.Return()))
    print("Total bet = " + str(player.totalBet) +  " total Return = " + str(player.totalReturn))
