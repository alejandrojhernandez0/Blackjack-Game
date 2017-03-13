# button.py
# for lab 8 on writing classes
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        self.text = label
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('black')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setFill('white')
        self.label.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        if(self.text == "EXIT"):
            self.rect.setFill('red')
            self.rect.setOutline('white')
            self.label.setFill('white')
            self.label.setStyle('bold')
            self.label.setSize(15)
            self.rect.setWidth(1)
            self.active = True
        else:
            self.rect.setFill('black')
            self.rect.setOutline('white')
            self.label.setFill('white') #color the text "black"
            self.rect.setWidth(1.5)       #set the outline to look bolder
            self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        "Sets this button to 'inactive'."
        ##color the text "darkgray"
        self.rect.setFill('grey')
        self.rect.setOutline('darkgrey')
        self.label.setFill('darkgray')
        ##set the outline to look finer/thinner
        self.rect.setWidth(3)
        ##set the boolean variable that tracks "active"-ness to False
        self.active=False

    ##check 4.  complete the clicked() method
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        ##your code here
    
        if  p.getX()>=self.xmin and p.getX()<=self.xmax and self.active==True:
            if p.getY()>=self.ymin and p.getY()<=self.ymax:
                return True
        else:
            return False 
