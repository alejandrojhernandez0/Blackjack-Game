from random import*
from graphics import*

#Alejandro Hernandez and Nina Cohen
#playingcardclass.py (Programming Assignment 5)
#11 November 2013
#COM 110

#Purpose: Gives blackjack values and the suits of each card
#for the deck to use in creating all 52 cards and putting them
#in the Blackjack game for use.
class PlayingCard:
    """PlayingCard gives you the suit and number of playing card, allows you
to enter the card youself and will return the blackjack value of it"""

    def __init__(self,suit,rank):

        #All possible suits/ranks
        suits = {"d":"Diamonds", "c":"Clubs", "s":"Spades", "h":"Hearts"}
        ranks = {1:"One", 2:"Two",3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
        self.rank = rank
        self.suit = suit

    #Gets the suit of the card
    def getSuit(self,suit):

        self.suit = suit
        
        if self.suit == "s":
            return "Spades"
        elif self.suit == "h":
            return "Hearts"
        elif self.suit == "c":
            return "Clubs"
        elif self.suit == "d":
            return "Diamonds"

    #Gets rank of card for determining Blackjack value
    def getRank(self,value):

        #Ace is by default 11, this could be changed [to 1]
        #later in the running of Blackjack if the values
        #of the other cards in hand necessitate so
        if value == 1:
            return 11
        
        if value == 2:
            return 2
        if value == 3:
            return 3
        if value == 4:
            return 4
        if value == 5:
            return 5
        if value == 6:
            return 6
        if value == 7:
            return 7
        if value == 8:
            return 8
        if value == 9:
            return 9
        if value == 10:
            value = 10
            return 10
        if value == 11:
            value = 10
            return 10
        if value == 12:
            value = 10
            return 10
        if value == 13:
            value = 10
            return 10

    #Returns blackjack valaue of card as integer
    #so it the Blackjack value can be addedin hand
    def __str__(self):
        return str(self.getRank(self.rank))

    #Draws the .gif image of the card that was drawn
    def draw(self, win, center):
        facecard = Image(center, "playingcards/" + str(self.suit) + str(self.rank) + ".gif")
        facecard.draw(win)



