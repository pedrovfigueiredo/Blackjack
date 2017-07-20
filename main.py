from deck import Deck
from player import Player
from dealer import Dealer

def printScore(players, dealer):
    print("\n--------\tScore\t--------")
    print("Dealer:", end=" ")
    print("Hand:", dealer.hand, end=" ")
    print("Sum:", dealer.getHandCount())
    print("----------------------------")
    for player in players:
        print(player.name + ":", end=" ")
        print("Hand:", player.hand, end=" ")
        print("Sum:", player.getHandCount())
        print("----------------------------")
    print("")

def printHands(players, dealer):
    print("\n--------\tHands\t--------")
    print("Dealer:", end=" ")
    print("Hand:", dealer.hand[0])
    print("----------------------------")
    for player in players:
        print(player.name + ":", end=" ")
        print("Hand:", player.hand, end=" ")
        print("Sum:", player.getHandCount())
        print("----------------------------")
    print("")

def printTotalMoney(players, dealer):
    print("\n-------- Total Money --------")
    print("Dealer:", dealer.total_money)
    print("-----------------------------")
    for player in players:
        print(player.name + ": " + str(player.total_money))
        print("-----------------------------")
    print("")

def clearHands(players):
    for player in players:
        player.hand.clear()
        player.sum_of_cards = 0

stop_game = False

while(stop_game == False):
    print("Starting new game...")

    # Ask how many players

    dealer = Dealer(10000)
    player = Player(1000, "Pedro")
    deck = Deck()

    while(True):

        player.betting_amount = float(input("Pick your betting amount: "))

        for aux in range(1,3): # Two cards for each player (including dealer)
            player.addCardToHand(deck.requestCard())
            dealer.addCardToHand(deck.requestCard())


        while(True):
            printHands([player], dealer)

            if player.getSingleCount() == 21: # Nothing more to do
                option = 'S'
                if len(player.hand) == 2: # Blackjack scenario
                    print("BLACKJACK!")
            else:
                option = input("Choose an option: ([S]tand or [H]it) ")

            if option.upper() == 'S':
                while(dealer.shouldStop() == False):
                    dealer.addCardToHand(deck.requestCard())
                break
            elif option.upper() == 'H':
                player.addCardToHand(deck.requestCard())
                if player.hasBusted():
                    print("Busted!")
                    break

        #   Results

        printScore([player], dealer)

        if player.hasBusted(): # dealer won
            player.total_money -= player.betting_amount
            dealer.total_money += player.betting_amount
            print("Dealer has won the round.")
        elif dealer.hasBusted(): # player won
            dealer.total_money -= player.betting_amount
            player.total_money += player.betting_amount
            print("Player has won the round.")
        elif dealer.getSingleCount() > player.getSingleCount(): # dealer won
            player.total_money -= player.betting_amount
            dealer.total_money += player.betting_amount
            print("Dealer has won the round.")
        elif dealer.getSingleCount() < player.getSingleCount(): # player won
            dealer.total_money -= player.betting_amount
            player.total_money += player.betting_amount
            print("Player has won the round.")
        else: # push
            print("Push!")

        printTotalMoney([player], dealer)
        option = input("Play next hand? ([Y]es or [N]o) ")

        if option.upper() == 'N':
            stop_game = True
            break

        clearHands([dealer,player])
        deck.shuffleCards()