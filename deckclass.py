from graphics import *
from playingcardclass import *
from random import *

#Alejandro Hernandez and Nina Cohen
#deckclass.py (Programming Assignment 5)
#COM 110

#Purpose: Creates all 52 cards in a deck by getting values and suits
#of each different card from the playingcard class. Also responsible
#for shuffling the deck and taking out cards as well
class Deck:

    def __init__(self):

        #Creating list for deck and declaring all 4 suits
        fulldeck = []
        suits = ["d","c","h","s"]

        self.cardList = fulldeck
        self.suits = suits

        #All 52 cards in deck are created here
        for s in self.suits:
            for r in range(1,14):
                self.cardList.append(PlayingCard(s,r))

    #Shuffles the deck of cards in random order
    def shuffleTheDeck(self):

        shuffled_Deck = {}
        
        for i in range(52):

            shuffle(self.cardList)

        #New shuffled deck is created every time deck
        #is shuffled
        shuffled_Deck = self.cardList

    #Takes a card from the shuffled deck
    def dealCard(self):

        shuffled_Deck = []
        
        for i in range(52):

            shuffle(self.cardList)

        shuffled_Deck = self.cardList
        card = shuffled_Deck[0]#Returns what card it is
        shuffled_Deck.remove(card)#Removes card from deck
        #once the card is taken
        shuffled_Deck = self.cardList
        return card

    #Returns how many cards are left
    def cardsLeft(self):

        current_deck = self.cardList
        print(len(current_deck))
          
