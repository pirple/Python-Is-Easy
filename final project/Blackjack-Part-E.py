##
# Blackjack, Part E Lecture
##

# _*_ coding: utf-8 _*_

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle              #import shuffle function from random module

def createDeck():                       #define a function to Create the Deck
    Deck = []                           #create Deck as a List

    faceValues = ["A", "J", "Q", "K" ]  #define faceValues with a list
    for i in range(4):                  #add values 4 times via a for loop so there are 4 different suits

        for card in range(2,11):        #loop through values between 2 to 10 not including 11. tese numbers represent cards
            Deck.append(str(card))      #add cards to Deck. converting Integers to Strins for more convinience
        for card in faceValues:         #loop through faceValues list
            Deck.append(card)           #add faceValues to Deck

    shuffle(Deck)                       #suffle the Deck
    return Deck                         #return the Deck

class Player:                              #here we will be creating Player class
    def __init__(self,hand = [],money = 100):        #__init__ function used to initialize a object. it is usually used to assign values for attributes of the object created by class
       self.hand =   hand              #define hand attribute for the class player
       self.score =  self.setScore()   #define score attribute for the Player and call to setScore function. return value from setScore will be assigned to score attribute
       self.money =  money             #define money attribute for the class player
       self.bet = 0                     #add a new attribute to Player called bet.

    def __str__(self):                 #overriding the __str__ function. it is used to print hand and score of the player
        CurrentHand = ""               #define a temporary variable to hold the current cards of the player
        for card in self.hand:         #loop through the player 'hand' and add each card to CurrentHand
            CurrentHand += str(card) + " "  #it is more convinient to add cards as strings to CurrentHand. so use str(card)

        finalStaus = CurrentHand + "score: " + str(self.score) #finalStaus will be in the format  "A 10 score:21"  "A 10 2 score:23"
        return finalStaus               #return finalStatus. which is printed by this function.

    def setScore(self):                 #define setScore method for player class
        self.score = 0                  #it is good practice to initialize the variable.
        faceCardsDict = {"A":11, "J":10, "Q":10, "K":10,            #create a Dictionary and map each card a value
                         "2":2, "3":3, "4":4, "5":5, "6":6,
                         "7":7, "8":8, "9":9, "10":10}
        aceCounter = 0                              #You need to count the number of Aces. here counter is initialized.
        for card in self.hand:                      #loop throught the hand of the player and add value of each card to players score
            self.score += faceCardsDict[card]
            if card == "A":                         #if the card is a Ace,
                aceCounter +=1                      #then increment the aceCounter
            if self.score > 21 and aceCounter != 0:  #if the acore is above 21 and player has a Ace
                self.score -= 10                     #new Ace value will be 1. hence score will be reduced by 10
                aceCounter -= 1                      #as one Ace is consumed, reduce 1 from aceCounter

        return self.score                            #return the score of the player

    def hit(self, card):                        #hit function is used to ada a card to hand
        self.hand.append(card)                  #new card will be append to the Player's hand
        self.score = self.setScore()            #player score will be recalculated

    def play(self, newHand):                    #play function will be used to restart the game or resest the hand. it will take a 'hand' as an argument
        self.hand = newHand                     #new hand will be assigned to Player's hand
        self.score = self.setScore()            #recalculate the Player's score

    def betMoney(self,amount):                  #change pay function to betMoney
        self.money -= amount                    #reduce bet amount from player's money
        self.bet += amount                      #add bet amount to Player's bet amount

    def win(self, result):                      #change win function. now it takes boolean argument.
        if result == True:                      #if win funtion recieve true
            if self.score == 21 and len(self.hand) == 2:   #if Blackjack is earned
                self.money += 2.5 * self.bet                #2.5 times of bet amount will be added to Player's money.
            else:                                   #if win but not a Blackjack
                self.money += 2 * self.bet          #two times of bet amount will be added to Players money
            self.bet = 0                        #we should erase bet amount after that
        else:
            self.bet = 0                        #if player is lost we only have to do erase bet amount. so it won't effect future play

def printHouse(House):                          #this method will print all cards of House except first card
    for card in range(len(House.hand)):         #loop through the hand of House
        if card == 0:                           #if it is the first card
            print("X", end=" ")                 #just print 'X'. continue printing in same line with space gap
        elif card == len(House.hand) - 1:       #if the card is the last one in the hand
            print(House.hand[card])             #just print it. no need of space
        else:                                   #else
            print(House.hand[card], end=" ")    #just print the card and keep a gap of space

cardDeck = createDeck()                             #what is returned from the createDeck() function will be assigned to 'cardDeck'
print(cardDeck)                                     #print the cardDeck
firstHand = [cardDeck.pop(),cardDeck.pop()]         #add last two cards to firstHand,
secondHand = [cardDeck.pop(),cardDeck.pop()]        #add next last two cards to secondHand
Player1 = Player(firstHand)                         #Player1 recieve firstHand
House = Player(secondHand)                          #House recieve secondHand
print(Player1)                                      #Print hand and score of Player1
printHouse(House)                                   #Print hand and score of House

while(Player1.score < 21):                          #this loop will continue as long as Player1 score is less than 21
    action = input("Do you want another card?(y/n)") #ask from user whether he needs another card. recieve user input
    if action == "y":                               #if he press 'y'
        Player1.hit(cardDeck.pop())                 #Player1 recieve a new card
        print(Player1)                              #Print hand and score of Player1
        printHouse(House)                           #Print hand and score of House
    else:
        break                                       #if user press 'n', exit the loop
