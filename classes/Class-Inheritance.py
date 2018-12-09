##
# Class Inheritance Lecture
##

# -*- coding: utf-8 -*-

class Team:        
    #constructor passes two variables Name and Origin. The
    #default value of variable Name is "Name" and that of variable Origin is "Origin".
    #If no values are passed through a constructor its default values are Name and Origin.
    def __init__(self, Name = "Name", Origin = "Origin"):             #constructor
        self.TeamName = Name                                          #member assignment
        self.TeamOrigin = Origin                                      #member assignment

    def DefineTeamName(self, Name):                                  #class method
        self.TeamName = Name

    def DefineTeamOrigin(self, Origin):                              #class method
        self.TeamOrigin = Origin

#class InheritanceClassName(ParentClass):
#    def __init__(self, Input1, Input2):
#        ParentClass.__init__(self)
#        self.Attribute1 = Input1
#        self.Attribute2 = Input2
#        self.Attribute3 = 0
#
#    def AnotherMethod(self):
#        Action(s)

'''
Class Player is derived from the base class or parent  class Team
'''
class Player(Team):
    def __init__(self):             #constructor
        Team.__init__(self)
        '''
        The __init__ method of our Team class explicitly invokes the __init__method of the Player class.
        '''
        self.PlayerName = "None"    #member variable assigned to None
        self.PlayerPoints = 0       #member variable assigned to 0

    '''
    Methods: ScoredPoints and setName
    ScoredPoints increments the PlayerPoints by 1.
    setName sets the name of Player
    '''
    def ScoredPoint(self):
        self.PlayerPoints += 1          #increments Playerpoints by 1

    def setName(self, name):
        self.PlayerName = name         #assigned name to Player


Player1 = Player()                    #create an instance of a class Player
print(Player1.PlayerName)             #print the value of member variable PlayerName
print(Player1.PlayerPoints)           #print the value of member variable PlayerPoints
Player1.DefineTeamName("Sharks")      #call methods DefineTeamName
print(Player1.TeamName)               #print the value of base class from derived class
print(Player1.TeamOrigin)             #print the value of member TeamOrigin of base class from derived class


class Player(Team):
    '''
    4 variables are passed into Contructor
    '''
    def __init__(self, PlayerName, PPoints, TeamName, TeamOrigin):
        Team.__init__(self, TeamName, TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoints = PPoints

    '''
    Methods: ScoredPoints and setName
    ScoredPoints increments the PlayerPoints by 1.
    setName sets the name of Player
    '''
    def ScoredPoint(self):
        self.PlayerPoints += 1

    def setName(self, name):
        self.PlayerName = name

    '''
    Override to print a readable string presentation of your object
    '''
    def __str__(self):
        return self.PlayerName + " has scored: " + str(self.PlayerPoints) + " Points"

Player1 = Player("Sid", 0, "Sharks", "Chicago")      #create an instance of a class Player
print(Player1.PlayerName)             #print the value of member variable PlayerName
print(Player1.PlayerPoints)           #print the value of member variable PlayerPoints
#Player1.DefineTeamName("Sharks")
print(Player1.TeamName)               #print the value of base class from derived class
print(Player1.TeamOrigin)             #print the value of member TeamOrigin of base class from derived class
Player1.ScoredPoint()                 #call method ScoredPoint
print(Player1.PlayerPoints)           #access member PlayerPoints from outside the class and print it
Player1.setName("Lee")                #call method setName
print(Player1.PlayerName)             #print the value of member variable PlayerName
print(Player1)                        #print the string message.
