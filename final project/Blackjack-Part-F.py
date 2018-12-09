##
# Blackjack, Part F Lecture
##

# _*_ coding: utf-8 _*_


from __future__ import print_function
#Import shuffle function from random library
from random import shuffle

# Set a createDeck function
def createDeck():
    Deck = []

    #Set a variable for faceValues
    faceValues = ['A', 'J', 'Q', 'K']
    for i in range(4): # There are 4 different suites
        for card in range(2,11): # Adding numbers 2-10
            Deck.append(str(card))

        for card in faceValues:
            Deck.append(card)

    shuffle(Deck) # Mixing results with shuffle
    return Deck # Return products

# Set a player class
class Player:
    def __init__(self,hand = [],money = 100):     #__init__ is the constructor for a class
      self.hand = hand
      self.score = self.setScore()
      self.money = money
      self.bet = 0

    def __str__(self):       #__str__ will return a human readable string
      currentHand = " "

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
    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()

    #Set a function to put out money
    def betMoney(self,amount):
        self.money -= amount          # Decrease money from balance
        self.bet += amount

    #Set a function for winner
    def win(self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2: # Set required score for winning blackjack
                self.money += 2.5*self.bet               # if player win with a blackjack
            else:
                self.money += 2*self.bet                 # if player win without a blackjack

            self.bet = 0                                 # Reset the bet
        else:
            self.bet = 0                                 # If player loose a bet

    #Set a function to check the result win or draw
    def draw(self):
		self.money += self.bet
		self.bet = 0

    #Set a function to check blackjack
    def hasBlackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
			return False


# Set a printHouse function to print the house and score
def printHouse(House):
    for card in range(len(House.hand)):
        if card == 0:
            print("X",end = " ")
        elif card == len(House.hand) -1:
			print(House.hand[card])
        else:
            print(House.hand[card], end = " ")

#Set a variable to createDock function, and then print it
cardDeck = createDeck()

# Pop function select the last shuffle number

# Set a variable for First players last shuffle number
firstHand =[cardDeck.pop(),cardDeck.pop()]

# Set a variable for Second players last shuffle number
secondHand = [cardDeck.pop(),cardDeck.pop()]

# Set a variable to First player score, and then print it
Player1 = Player(firstHand)

# Set a variable to Second player score, and then print it
House = Player(secondHand)

cardDeck = createDeck()

while(True):
    if len(cardDeck) <20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    Player1.play(firstHand)
    House.play(secondHand)

    # Set a variable to ask player for bet amount
    Bet = int(input("Please enter your bet: "))

    print(cardDeck)
    Player1.betMoney(Bet)
    printHouse(House)
    print(Player1)

    #Define results on Blackjack win
    if Player1.hasBlackjack():
        if House.hasBlackjack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        # if players score is below 21, ask him to add more card
        while(Player1.score < 21):# While (true==true)
            action = input("Do you want another card?(y/n): ")
            if action == "y":
                Player1.hit(cardDeck.pop())
                print(Player1)
                printHouse(House)
            else:
                break
        # Define how long player can add card
        while(House.score < 16):
            print(House)
            House.hit(cardDeck.pop())

        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
            else:
                Player1.win(False)

        elif Player1.score > House.score:
            Player1.win(True)

        elif Player1.score == House.score:
            Player1.draw()

        else:
            if House.score > 21:
                Player1.win(True)
            else:
                Player1.win(False)

    print(Player1.money)
    print(House)
