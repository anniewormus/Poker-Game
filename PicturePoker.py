''' 
    This is a simple poker game that has the same rules as the Mario Picture Poker
    Game.
    Created by Annie Wormus 9/23/2021
'''
# IMPORTS
import time
from resources import table, welcomeBanner
import random 

heart = "\u2665"
smile = "\u263B"
music = "\u266A"
star = "*"
club = "\u2663"
o = "o"

cards = [heart, smile, music, star, club, o]

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def set_up():
# Set up function that determines player name, how many other players
    ''' 
        Returns:
                *NONE*
    '''

    print(welcomeBanner)

    repeatFlag = True

    while repeatFlag:

        print("Would you like to start the game (Y/N)?")

        start = input()
        if start == "Y" or start == "y" or start == "yes":
            play_game(0, 5)
            repeatFlag = False
        elif start == "N" or start == "n" or start == "no":
            exit_game()
        else:
            print("I'm sorry, I didn't understand your response.")
        
'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def play_game(round, chips):
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
    inputFlag = True

    #while winnings > 0 or stopGame:
    round += 1
    # print round stats
    round_stats(round, chips)
    # deals starting hand / pre-flop
    deal_starting_hand(hand)
    # prints hand for player
    print_hand(hand)

    betFlag = False

    while betFlag == False:
        betFlag = bet(chips)
    
    playerCall = input()
    while inputFlag:
        print("Would you like to 1) trade or 2) hold")
        playerCall = input()

        if playerCall == "1":
            print("player checked")
            inputFlag = False
        elif playerCall == "2":
            print("player betted")
            inputFlag = False
        else:
            print("Please enter a valid option.")

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''   
def bet(chips):
    print("How much would you like to bet?")
    betValue = int(input())

    if betValue > chips:
        print("You don't have enough chips, try again")
        return False
    else:
        return True

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''   
def deal_starting_hand(hand):
# Deals the starting hand to player: two random cards
    '''
        Variables: 
                   hand[] - cards in players hand
        Returns: 
                *NONE*
    '''
    print("Your hand:")
    i = -1
    for x in hand:
        i += 1
        hand[i] = "[" + deal_card() + "]"

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def round_stats(roundNum, chips):
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
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print(table)
    print("Chips: ",end="")
    while chips > 0:
        print("o ", end="")
        chips -= 1
    print("\n")
    
'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def deal_card():
# Generates a random card as if it were drawn from a deck
    '''
        Variables: 
                    card - string, card dealt
                    number - int, number of card dealt 1-10 or J, Q, K, A
        Returns: 
                card - string,  ♥ ☻ ♪ ♦ * ♣ o
    '''
    # Variable Set Up
    number = random.randint(0, 5)
    card = cards[number]

    return card

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
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
    
    print()

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def print_pot():
    print("You have ")

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def exit_game():
# Ends game for player and quits program
    print("Goodbye!")
    exit()

set_up()