''' 
    This program is a simple python script that emulates a poker game
    Created by Annie Wormus 9/23/2021
'''
# Resource file for animated pictures
table = """
[♥]             (._.)
[☻]       _________________      
[♪]       |   [][][][][]  |
[*]       |      ooo o    |
[♣]       |_______________|  
[o]
    """
welcomeBanner = """
+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
           Picture Poker
+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
Welcome to the Picture Poker Lobby!

Get a better hand than Winston to win!
If you're confident in your hand,
increase the number of chips you bet!
    """
helpMenu = """
Here are some rules for you before 
you begin:
1. You start with 5 chips and 5 cards
2. The different cards will be displayed
    on the left hand side of your screen 
    in order from high cards at the top
    to low cards at the bottom
3. Each round consists of a bet and 
    trading of cards
4. The possible hands you can have go
    as follows, in order from highest
    to lowest:
    Flush/Five of a kind:
                        [♥][♥][♥][♥][♥]
    Four of a kind:
                        [*][*][*][*][♦]
    Full House:
                        [☻][☻][☻][♣][♣]
    Three of a kind:
                        [♪][♪][♪][♦][o]
    Two Pairs:
                        [o][o][♪][♪][♥]
    One Pair:
                        [♣][♣][☻][*][♦]
    """
