from deck import Deck
from player import Player
from dealer import Dealer
from generic_player import Generic_Player

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
    for player in players:
        print(player.name + ": " + str(player.total_money))
        print("-----------------------------")
    print("")

def clearHands(players: Generic_Player):
    for player in players:
        player.hand.clear()
        player.sum_of_cards = 0


while True:
    print("Starting new game...")

    # Ask how many players

    players_count = int(input("How many players are going to play? "))
    while players_count < 1:
        players_count = input("Incorrect value.\n How many players are going to play?")

    deck = Deck()
    dealer = Dealer()
    players = []

    for count in range(players_count):
        name = input("Insert player's name: ")
        start_money = float(input("Insert initial money: "))
        players.append(Player(start_money, name))
    active_players = list(players)

    while any(player.stopped_playing == False for player in players):

        for player in active_players:
            print(player.name + ": ")
            player.betting_amount = float(input("Pick your betting amount: "))

        for aux in range(1,3): # Two cards for each player (including dealer)
            for player in active_players:
                player.addCardToHand(deck.requestCard())
            dealer.addCardToHand(deck.requestCard())

        printHands(active_players, dealer)


        for player in active_players:
            if player.getSingleCount() == 21: # Nothing more to do
                option = 'S'
                if len(player.hand) == 2: # Blackjack scenario
                    print("BLACKJACK!")
            else:
                while(True):
                    print(player.name + ":")
                    option = input("Choose an option: ([S]tand, [H]it, Sho[W] Hand) ")
                    if option.upper() == 'W':
                        printHands(active_players, dealer)
                        continue
                    break

            while option.upper() == 'H':
                player.addCardToHand(deck.requestCard())
                if player.hasBusted():
                    print("Busted!")
                    break
                printHands(active_players, dealer)
                print(player.name + ":")
                option = input("Choose an option: ([S]tand, [H]it, Sho[W] Hand) ")

        while (dealer.shouldStop() == False):
            dealer.addCardToHand(deck.requestCard())

        #   Results

        printScore(active_players, dealer)

        if dealer.hasBusted(): # players won
            for player in active_players:
                if player.hasBusted():
                    player.total_money -= player.betting_amount
                    print(player.name + " LOSE")
                else:
                    player.total_money += player.betting_amount
                    print(player.name + " WIN")
        else:
            for player in active_players:
                if player.hasBusted() == True or player.getSingleCount() < dealer.getSingleCount():
                    player.total_money -= player.betting_amount
                    print(player.name + " LOSE")
                elif player.getSingleCount() > dealer.getSingleCount():
                    player.total_money += player.betting_amount
                    print(player.name + " WIN")
                else:
                    print(player.name + " PUSH")

        printTotalMoney(active_players, dealer)
        for player in active_players:
            print(player.name + ":")
            option = input("Play next hand? ([Y]es or [N]o) ")
            if option.upper() == 'N':
                player.stopped_playing = True

        for player in players:
            if player.stopped_playing == True and player in active_players:
                active_players.remove(player)

        clearHands(active_players + [dealer])

        deck.shuffleCards()

    print("Final Board:")
    printTotalMoney(players,dealer)
    end_game = input("\nRestart? [Y]es or [N]o ")

    if end_game.upper() == 'N':
        break

print("\n\nThank you for playing my blackjack game!")
print("See you on the next one!")