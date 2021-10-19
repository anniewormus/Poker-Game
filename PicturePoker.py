''' 
    This is a simple poker game that has the same rules as the Mario Picture Poker
    Game.
    Created by Annie Wormus 9/23/2021
'''
# IMPORTS
import time
from resources import table, welcomeBanner, card_placements
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
    

    #while winnings > 0 or stopGame:
    round += 1
    # print round stats
    round_stats(round, chips)
    # deals starting hand / pre-flop
    deal_starting_hand(hand)
    # prints hand for player
    print_hand(hand)
    # gets players initial bet
    playerBet = bet(chips)
    # gives player option to trade or hold their cards
    tradeOrHold(hand)

    print("\nFinal hand: ")
    print_hand(hand)

    # sortHand(hand)

    calculateWinnings(hand)
    
    
'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''   
def calculateWinnings(hand):
    handCount = [0, 0, 0, 0, 0]
    i = 0
    for x in hand:
        for y in cards:
            if x == "[" + y + "]":
                handCount[cards.index(y)] += 1
    
    i = 0
    for i in range(5):
        print(handCount[i], end=" "),
  

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def tradeOrHold(hand):
# Lets play make option to trade their cards or hold their cards
# If player trades cards they get replaced, and if player holds cards they move
# on to the next step
    '''
        Variables: 
                inputFlag - boolean determining if the player chose a valid 
                            input
                playerCall - 1) trade 2) hold
                tradeNum - number of cards player wants to trade
                tradingCard - index of card player wants to trade

        Returns: 
                *NONE*
    '''

    inputFlag = True

    # Loops through until player makes a valid option choice
    while inputFlag:
        print("Would you like to 1) trade or 2) hold")
        playerCall = input()

        # Trade cards selected
        if playerCall == "1":
            print("How many cards would you like to trade?")
            tradeNum = int(input())

            # Gets all indecies of cards player wants to trade
            i = 0
            while i < tradeNum:
                print("Please enter the spot number of the card ", i+1, ": ")
                print_hand(hand)
                tradingCard = int(input())
                hand[tradingCard-1] = "   "
                i += 1
            # Replaces traded cards with new cards
            i = 0
            for x in hand:
                if x == "   ":
                    hand[i] = "[" + deal_card() + "]"
                i += 1
            inputFlag = False
        # Hold cards selected
        elif playerCall == "2":
            inputFlag = False
        # Invalid option selected
        else:
            print("Please enter a valid option.")
'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''   
def bet(chips):
# Asks player to enter a valid bet value
    '''
        Variables: 
                betFLag - keeps track of whether player input is valid
                        i.e. the bet is less than or equal to the number
                        of player chips
                betValue - wager of player
        Returns: 
                a valid number of chips the player wants to be
    '''
    betFlag = True
    betValue = 0

    # Loops through until player bets a valid number of chips
    while betFlag == True:
        print("How much would you like to bet?")
        betValue = int(input())
        # If the players eyes are bigger than their wallet
        if betValue > chips:
            print("You don't have enough chips, try again")
        else:
            betFlag = False

    return betValue

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
    # Populates hand array with cards
    i = 0
    for x in hand:
        hand[i] = "[" + deal_card() + "]"
        i += 1

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
    i = 0
    while i < chips:
        print("o ", end="")
        i += 1
    print("\t(", chips, ")\n")
    
'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def deal_card():
# Generates a random card as if it were drawn from a deck
    '''
        Variables: 
                card - string, card dealt
                number - int, number of card dealt 1-10 or J, Q, K, A
        Returns: 
                card - string,  ♥ ☻ ♪ * ♣ o
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
                *NONE*    
        Returns: 
                *NONE*
    '''
    i = 0
    for i in range(5):
        print(hand[i], end=" "),
    
    print(card_placements)

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
def exit_game():
# Ends game for player and quits program
    print("Goodbye!")
    exit()

set_up()