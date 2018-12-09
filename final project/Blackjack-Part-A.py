##
# Blackjack, Part A Lecture
##

# _*_ coding: utf-8 _*_

#Import shuffle function from random library
from random import shuffle

# Create a functions
def createDeck():
    Deck = []
    #Set a variable for faceValues
    faceValues = ['A', 'J', 'Q', 'K']
    for i in range(4): #There are 4 different suites
        for card in range(2,11): #Adding numbers 2-10
            Deck.append(str(card))

        for card in faceValues:
            Deck.append(card)
    return Deck #Return products

#Set a variable to createDock function, and then print it
cardDeck = createDeck()

shuffle(cardDeck) #Mixing results with shuffle

print(cardDeck)
