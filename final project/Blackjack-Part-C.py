##
# Blackjack, Part C Lecture
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
    shuffle(Deck) #Mixing results with shuffle
    return Deck #Return products

#Set a variable to createDock function, and then print it
cardDeck = createDeck()
print(cardDeck)

# Set a player class
class Player:
    def __init__(self,hand = [],money = 100): #__init__ is the constructor for a class
      self.hand = hand
      self.score = self.setScore()
      self.money = money

    def __str__(self): #__str__ will return a human readable string
      currentHand = " " #slef.hand = ["A","10"]

      for card in self.hand:
          currentHand  += str(card) + " "

      #Set a variable for finalStatus, and then return it
      finalStatus = currentHand + "score " + str(self.score)
      return finalStatus

    #Set a setScore function to count score, and then return it
    def setScore(self) :
        self.score = 0
        #Set a Dictionary for faceCards
        faceCardsDict = {"A":11,"J":10,"Q":10,"K":10,
                        "2":2,"3":3,"4":4,"5":5,"6":6,
                        "7":7,"8":8,"9":9,"10":10}
        #Set a variable for aceCounter
        aceCounter = 0
        #Convert card into score
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter +=1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1

        return self.score

    #Set a hit function to select a card, and then return it
    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()

    #Set a function to add new player
    def play(self,newHnad):
        self.hand = newHnad
        self.score = self.setScore()

    #Set a function to put out money
    def pay(self,amount):
        self.money -= amount #decrease money from balance

    #Set a function for winner
    def win(self,amount):
        self.money += amount # double amount for winner


#Set a variable for player1, and then print it
Player1 = Player(["3","7","5"])
print(Player1)
Player1.hit("A")
Player1.hit("A")
print(Player1) #Score after selecting a card
Player1.pay(20)
print(Player1.money) #Balance after puting money
Player1.win(40)
print(Player1.money) #Balance after winning
Player1.play(["A","K"])
print(Player1) #Score for new player
print(Player1.money) #After restarting the game
