''' 
    This program is a simple python script that emulates a poker game
    Created by Annie Wormus 9/23/2021
'''
# IMPORTS

import time
from resources import table
import random 

# Game set up
suites = ["\u2660", "\u2665", "\u2663", "\u2666"]
royal = ["K", "Q", "J", "A"]

def set_up():
# Set up function that determines player name, how many other players
    ''' 
        Returns:
                *NONE*
    '''
    welcomeBanner = """
    +-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
                 Welcome
    +-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
    """
    print(welcomeBanner)

    print("Please enter your name: ")
    playerName = input()
    print("Hello " + playerName)
    
    print(table)

    print("Would you like to start the game (Y/N)?")

    start = input()
    if start == "Y" or start == "y" or start == "yes":
        play_game(playerName, 1, 500)
    else:
        exit_game()

def play_game(playerName, round, winnings):
# Loops through rounds of the game until player runs out of money
# or manually exits the game
    '''
        Variables: 
                    stopGame - boolean, stops game / exits loop
                    dealerNum - int, states which player is the dealer 
                                for the current round
        Returns: 
                *NONE*
    '''
    # Variable Set Up
    stopGame = False
    hand = ["", "", "", "", ""]
    round = 0
    inputFlag = False


    #while winnings > 0 or stopGame:
    round += 1
    round_stats(round, winnings)

    print("Your hand:")
    hand[0] = "[" + deal_card() + "]"
    hand[1] = "[" + deal_card() + "]"
    print_hand(hand)

    while inputFlag == False:
        print("\nWould you like to 1) Check 2) Bet or 3) Fold?")
        playerCall = input()

        if playerCall == "1":
            print("player checked")
            inputFlag = True
        if playerCall == "2":
            print("player betted")
            inputFlag = True
        if playerCall == "3":
            print("player folded")
            inputFlag = True
        else:
            print("Not a valid option.")
    


def round_stats(roundNum, winnings):
# Prints round stats - player earnings, and round number
    '''
        Variables: 
                    roundNum - round number
                    winnings - total money player has
        Returns: 
                *NONE*
    '''
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print("\t\tROUND ", roundNum)
    print("Your winnings: $", winnings)
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print(table)

def deal_card():
# Generates a random card as if it were drawn from a deck
    '''
        Variables: 
                    card - string, card dealt
                    number - int, number of card dealt 1-10 or J, Q, K, A
                    suiteNum - number rep of suite ♣, ♦, ♠, ♥
                    royalNum - number rep of face card J, Q, K, A
        Returns: 
                card - string, representation of a number 1-10 or J, K, Q, A
                        and suite ♣, ♦, ♠, ♥
    '''
    # Variable Set Up
    card = ""
    number = random.randint(1, 14)
    suiteNum = random.randint(0, 3)
    suite = suites[suiteNum]

    # If the number is greater than 10, turn it into the corresponding
    # royal card
    if number > 10:
        number = number % 11
        royalnum = royal[number]
        card = royalnum + suite
    else:
        card = str(number) + suite

    return card

def print_hand(hand):
# Prints out players current hand
    '''
        Variables: 
                    
        Returns: 
                *NONE*
    '''
    i = 0
    for i in range(5):
        print(hand[i], end=" "),


def exit_game():
# Ends game for player and quits program
    print("Goodbye!")
    exit()

set_up()