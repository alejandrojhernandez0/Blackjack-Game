from graphics import *
from deckclass import *
from playingcardclass import *
from button import *
from time import *

#Alejandro Hernandez and Nina Cohen
#blackjackclass.py (Programming Assignment 5)
#11 November 2013
#COM 110

#Purpose: Create a blackjack game application using class interaction
#and GUI, the game should be user friendly and replayable.
class Blackjack:

    #Default constructor for keeping the player and dealer hands
    #as well as initializing the default deck
    def __init__(self, dHand = [], pHand = []):
        """constructor that initializes instance variables,
        it also gives the playingDeck and initial shuffle"""
        self.dealerHand = dHand
        self.playerHand = pHand
        self.deck = Deck()
        self.deck.shuffleTheDeck()
        #Deck is shuffled by default once program is run

    #Constructor for handing out the first 2 cards
    def initDeal(self,gwin):
        """deals out initial cards, 2 per player and displays
        dealer and player hands on graphical win, xposD and
        yposD give initial position for dealer cards, xposP
        and yposP are analogous"""
        #First two cards for the dealer, initially covered
        #by the cover cards
        dCard1 = self.deck.dealCard()
        dCard1.draw(gwin,Point(50,150))
        dCovercard1 = Image(Point(50,150),"playingcards/b2fv.gif")
        dCovercard1.draw(gwin)
        dCard2 = self.deck.dealCard()
        dCard2.draw(gwin,Point(100,150))
        dCovercard2 = Image(Point(100,150),"playingcards/b2fv.gif")
        dCovercard2.draw(gwin)

        #First two cards are added to dealers deck
        self.dCover1 = dCovercard1
        self.dCover2 = dCovercard2
        self.dealerHand.append(dCard1)
        self.dealerHand.append(dCard2)

        #First two cards for the player, initially covered
        #by the cover cards
        pCard1 = self.deck.dealCard()
        pCard1.draw(gwin,Point(50,300))
        pCovercard1 = Image(Point(50,300),"playingcards/b1fv.gif")
        pCovercard1.draw(gwin)
        pCard2 = self.deck.dealCard()
        pCard2.draw(gwin,Point(100,300))
        pCovercard2 = Image(Point(100,300),"playingcards/b1fv.gif")
        pCovercard2.draw(gwin)

        #First two cards are added to players deck
        self.pCover1 = pCovercard1
        self.pCover2 = pCovercard2
        self.playerHand.append(pCard1)
        self.playerHand.append(pCard2)

    #Constructor for when player hits
    def hit(self,gwin,xPos,yPos):
        """adds a new card to the player's hand and places it
        at xPos, yPos"""
        #New card in taken out of deck and added to player's hand
        new_pCard = self.deck.dealCard()
        new_pCard.draw(gwin,Point(xPos,yPos))
        self.playerHand.append(new_pCard)
        
        self.dCover1.undraw()
        self.dCover2.undraw()

        self.pCover1.undraw()
        self.pCover2.undraw()

    #Constructor for evaluate the hand of either the dealer or the
    #player
    def evaluateHand(self,hand):
        """totals the cards in the hand that is passed in and
        returns total (ace counts as 11 if doing so allows total
        to stay under 21)"""
        self.total = 0
        HighAceCount = 0
        for card in hand:
            #This large part takes into account the ace, which has a default
            #value of 11, the determined value of the ace or aces will
            #depend on what the values of the other cards in the hand
            #are
            if(int(card.__str__()) == 11):
                if(int(card.__str__()) + self.total <= 21):
                    self.total = self.total + 11
                    HighAceCount += 1
                elif(int(card.__str__()) + self.total == 11):
                    self.total = self.total + 11  
                else:
                    self.total = self.total + 1
            elif(HighAceCount > 0):
                if(self.total + int(card.__str__()) > 21):
                    self.total = (self.total + int(card.__str__())) - 10
                    HighAceCount -= 1
                else:
                    self.total = self.total + int(card.__str__())

            #This adds cards that are not aces
            else:
                self.total = self.total + int(card.__str__())
                
        return self.total

    #The dealer hits, note that this constructor will not be
    #run if the dealer is at soft 17 or over it
    def dealerPlays(self,gwin,xPos,yPos):
        """dealer deals cards to herself, stopping when hitting
        "soft 17" """
        #Same thing as hit, except a new card drawn from the deck
        #is added to the dealers hand
        new_dCard = self.deck.dealCard()
        new_dCard.draw(gwin,Point(xPos,yPos))
        self.dealerHand.append(new_dCard)

    #This is just a simple construtor that takes off the colored card covers
    #once the game begins
    def uncover(self):

        self.dCover1.undraw()
        self.dCover2.undraw()

        self.pCover1.undraw()
        self.pCover2.undraw()

    #Takes the current hand of the dealer
    def dHand(self):

        return self.dealerHand

    #Takes the current hand of the player
    def pHand(self):

        return self.playerHand

    #Erases all the cards in the player and dealer hands, this is necessary
    #for starting a new game once a blacjack game is over
    def reset(self,hand):

        del hand[:]

#Runs the game    
def game():

    #Starts the game screen:
    gwin = GraphWin("Blackjack Table",600,600)
    gwin.setBackground("darkgreen")
    
    #---GAME SCREEN GUI---
    toptxt = Text(Point(300,15),"Game Screen")
    toptxt.setTextColor("white")
    toptxt.setStyle("bold")
    toptxt.setSize(8)
    toptxt.draw(gwin)

    dealertxt = Text(Point(75,80),"Dealer")
    dealertxt.setTextColor("white")
    dealertxt.setStyle("bold")
    dealertxt.setSize(12)
    dealertxt.draw(gwin)

    playertxt = Text(Point(75,370),"You")
    playertxt.setTextColor("white")
    playertxt.setStyle("bold")
    playertxt.setSize(12)
    playertxt.draw(gwin)

    cardtxt = Text(Point(525,15),"Card Values:")
    cardtxt.setTextColor("white")
    cardtxt.setStyle("bold")
    cardtxt.setSize(8)
    cardtxt.draw(gwin)

    valtxt1 = Text(Point(525,30),"2-10: Number of the card")
    valtxt1.setTextColor("white")
    valtxt1.setStyle("bold")
    valtxt1.setSize(8)
    valtxt1.draw(gwin)

    valtxt2 = Text(Point(525,45),"J,Q,K: 10")
    valtxt2.setTextColor("white")
    valtxt2.setStyle("bold")
    valtxt2.setSize(8)
    valtxt2.draw(gwin)

    valtxt3 = Text(Point(525,60),"A: 1 or 11")
    valtxt3.setTextColor("white")
    valtxt3.setStyle("bold")
    valtxt3.setSize(8)
    valtxt3.draw(gwin)

    note = Text(Point(110,30),"*The dealer will stand (not hit) if the")
    note.setTextColor("white")
    note.setStyle("bold")
    note.setSize(8)
    note.draw(gwin)

    note2 = Text(Point(110,45),"cards add to 17 (soft 17) or over!")
    note2.setTextColor("white")
    note2.setStyle("bold")
    note2.setSize(8)
    note2.draw(gwin)
    
    dealButton = Button(gwin, Point(300,515), 100, 30, "Deal")
    hitButton = Button(gwin, Point(400,455), 100, 30, "Hit")
    standButton = Button(gwin, Point(200,455), 100, 30, "Stand")
    exitButton = Button(gwin, Point(555,570), 50, 40, "EXIT")
    #---GAME SCREEN GUI---

    #Activation/Deactivation of buttons before game
    #starts, dealButton will commence a game, exitButton
    #will exit out of window. The other buttons are
    #not availible until game commences.
    dealButton.activate()
    exitButton.activate()
    hitButton.deactivate()
    standButton.deactivate()

    #A game of blackjack is started
    blackjack = Blackjack()
    blackjack.__init__()
    blackjack.initDeal(gwin)

    #Other GUI graphics
    totalsquare = Rectangle(Point(15,580),Point(100,520))
    totalsquare.setFill("black")
    Ototal = Text(Point(60,545),"Your total:")
    Ototal.setFill("white")
    Ototal.setStyle("bold")
    Ototal.setSize(10)
    totalsquare.draw(gwin)
    Ototal.draw(gwin)

    #--Defualt strings for ending GUI prompt--
    output = ""
    pBlackjack = ""
    dBlackjack = ""

    #Default position for a drawn card, this
    #position will be increased to further
    #accomodate more cards if possible
    P_hitPos = 125
    D_hitPos = 125

    #Runs the game in loop
    cont = True
    pt = gwin.getMouse()
    while (cont == True):

        if dealButton.clicked(pt) == True:
            #Now that the deal button is clicked, the game buttons
            #(hit and stand) are activated and ready to be clicked
            hitButton.activate()
            standButton.activate()
            dealButton.deactivate()
            Covercard = Image(Point(100,150),"playingcards/b2fv.gif")
            Covercard.draw(gwin)
            blackjack.uncover()
            total = Text(Point(55,565),blackjack.evaluateHand(blackjack.pHand()))
            total.setSize(17)
            total.setFill("white")
            total.draw(gwin)

        #If hit button is clicked, card is drawn, this can be done multiple
        #times until player busts or chooses to stand
        elif hitButton.clicked(pt) == True:
            total.undraw()
            hit = blackjack.hit(gwin,P_hitPos,300)
            P_hitPos += 25 #Position accumulates to accomodate more cards in hand if needed
            total = Text(Point(55,565),blackjack.evaluateHand(blackjack.pHand()))
            total.setSize(17)
            total.setFill("white")
            total.draw(gwin)
            if(int(blackjack.evaluateHand(blackjack.pHand()) > 21)):
                #If player busts the game screen will give the message below
                output = "You busted! Dealer wins!"
                
                
                if(int(blackjack.evaluateHand(blackjack.dHand())) == 21):
                    #If the dealer has cards that add to 21, the screen will give message below
                    dBlackjack = "Blackjack!"
                break

        #If stand button is clicked, player is no longer active and dealer will
        #hit until soft 17 or over, the dealer can bust just like the player
        elif standButton.clicked(pt)== True:
            #The check for soft 17 or over
            sleep(.4)
            Covercard.undraw()
            sleep(.4)
            while(int(blackjack.evaluateHand(blackjack.dHand())) < 17):
                sleep(.3)
                dealerTurn = blackjack.dealerPlays(gwin,D_hitPos,150)
                D_hitPos += 25 #Position accumulates to accomodate more cards in hand if needed
                blackjack.evaluateHand(blackjack.dHand())
                sleep(.3) #Short pause between drawn cards
                if(int(blackjack.evaluateHand(blackjack.dHand()) > 21)):
                    #If dealer busts the game screen will give the message below
                    output = "Dealer busted! You win!"
                    if(int(blackjack.evaluateHand(blackjack.pHand())) == 21):
                        #If the player has cards that add to 21, the screen will give message below
                        pBlackjack = "Blackjack!"
                    break

            #These game messages will show if the dealer and the player end up standing and do not bust:
            Covercard.undraw()
            #If the dealer is closer to 21 (no bust) than the player, the dealer wins and the screen will print such
            if(int(blackjack.evaluateHand(blackjack.dHand())) > int(blackjack.evaluateHand(blackjack.pHand()))):
                if(int(blackjack.evaluateHand(blackjack.dHand())) <= 21):
                    output = "Dealer wins!"
                    #If dealer wins with a blackjack hand, screen will print so
                    if(int(blackjack.evaluateHand(blackjack.dHand())) == 21):
                        dBlackjack = "Blackjack!"
                    break
                else:
                    break

            #If the player is closer to 21 (no bust) than the dealer, the player wins and the screen will print such
            elif(int(blackjack.evaluateHand(blackjack.dHand())) < int(blackjack.evaluateHand(blackjack.pHand()))):
                if(int(blackjack.evaluateHand(blackjack.pHand())) <= 21):
                    output = "You win!"
                    #If player wins with a blackjack hand, screen will print so
                    if(int(blackjack.evaluateHand(blackjack.pHand())) == 21):
                        pBlackjack = "Blackjack!"
                    break
                else:
                    break

            #This is just in case there is a tie where both the dealer and the player ultimately have the same total (No bust)
            elif(int(blackjack.evaluateHand(blackjack.dHand())) == int(blackjack.evaluateHand(blackjack.pHand()))):
                if(int(blackjack.evaluateHand(blackjack.pHand())) <= 21):
                    output = "Push"
                    #If both player and dealer 'push' with blackjack hands, then screen will print so
                    if(int(blackjack.evaluateHand(blackjack.pHand())) == 21):
                        pBlackjack = "Blackjack!"
                        dBlackjack = "Blackjack!"
                    break
                else:
                    break

        #Anytime exit button is clicked, the game window will close
        elif exitButton.clicked(pt) == True:
            gwin.close()

        pt = gwin.getMouse()

    #This is the GUI for displaying who won, busted, got blackjack, etc.
    text = Text(Point(300,420),output)
    text.setFill("white")
    text.setStyle("bold")
    text.setSize(14)
    text.draw(gwin)

    text = Text(Point(150,370),pBlackjack)
    text.setFill("red")
    text.setStyle("bold")
    text.setSize(12)
    text.draw(gwin)
    
    text = Text(Point(150,80),dBlackjack)
    text.setFill("red")
    text.setStyle("bold")
    text.setSize(12)
    text.draw(gwin)

    #The game restarts again, button activation is reset
    dealButton.activate()
    hitButton.deactivate()
    standButton.deactivate()

    #A new game will commence once deal button is clicked,
    #everything is reset and a new shuffled deck is made
    #for the next game. If the user clicks the exit button
    #the window will close
    pt = gwin.getMouse()
    while(exitButton.clicked(pt) == False):
        if(dealButton.clicked(pt) == True):
            gwin.close()
            blackjack.reset(blackjack.dHand())
            blackjack.reset(blackjack.pHand())
            game() #Activates a new game again
        pt = gwin.getMouse()

    gwin.close()
    
def main():

    #---INTRO SCREEN GUI---
    win = GraphWin("Blackjack",600,600)
    win.setBackground("darkgreen")
    
    title = Text(Point(300,125),"Welcome to Blackjack!")
    title.setTextColor("white")
    title.setStyle("bold")
    title.setSize(25)
    title.draw(win)

    names = Text(Point(440,580),"Made by: Alejandro Hernandez and Nina Cohen")
    names.setTextColor("white")
    names.setStyle("bold")
    names.setSize(10)
    names.draw(win)

    img1 = Image(Point(290,280),"playingcards/s1.gif")
    img1.draw(win)
    img2 = Image(Point(315,290),"playingcards/s13.gif")
    img2.draw(win)

    txt = Text(Point(300,375),"Whoever gets closest to 21 wins!")
    txt.setTextColor("white")
    txt.setStyle("bold italic")
    txt.setSize(18)
    txt.draw(win)

    #---INSTRUCTIONAL PROMPT---
    rules = Text(Point(300,485),"Basic Rules:")
    rules.setTextColor("white")
    rules.setStyle("bold")
    rules.setSize(9)
    rules.draw(win)

    rLine1 = Text(Point(300,505),"Two cards are dealt, the player can choose to either hit or stand. If the player hits then an extra")
    rLine1.setTextColor("white")
    rLine1.setStyle("bold")
    rLine1.setSize(8)
    rLine1.draw(win)

    rLine2 = Text(Point(300,520),"card is drawn from the deck and added to the hand, but if the added cards are over 21, then the player")
    rLine2.setTextColor("white")
    rLine2.setStyle("bold")
    rLine2.setSize(8)
    rLine2.draw(win)

    rLine3 = Text(Point(300,535),"will bust and lose the game. If the player stands then the dealer will hit unless the dealer is at soft")
    rLine3.setTextColor("white")
    rLine3.setStyle("bold")
    rLine3.setSize(8)
    rLine3.draw(win)

    rLine4 = Text(Point(300,550),"17 or over. If not, then the dealer will hit until the cards add up to 17 or over. The dealer can also bust.")
    rLine4.setTextColor("white")
    rLine4.setStyle("bold")
    rLine4.setSize(8)
    rLine4.draw(win)
    #---INSTRUCTIONAL PROMPT---

    #---START BUTTON GUI---
    button = Rectangle(Point(230,420),Point(375,470))
    button.setFill("black")
    button.setOutline("darkgrey")
    button.setWidth(3)
    button.draw(win)
    buttonText = Text(Point(302.5,445),"Start")
    buttonText.setFill("white")
    buttonText.setStyle("bold")
    buttonText.setSize(16)
    buttonText.draw(win)
    #---START BUTTON GUI---
    #---INTRO SCREEN GUI---
    
    #Checking for start button click:
    start = False
    while(start == False):

        #If start button is clicked, then the blackjack game
        #will run in a new window, the intro window will close
        #after blackjack game is opened.
        pt = win.getMouse()
        if(pt.getY() >= 420 and pt.getY() <= 470):
            if(pt.getX() >= 230 and pt.getX() <= 375):
                win.close()
                game()
                
main()

        
        
