##
# Introduction to Classes Lecture
##

# -*- coding: utf-8 -*-


"""
class is defined by a keyword class

Classname Team in defined
"""

class Team:
    def __init__(self):                          #constructor with no arguments
        self.TeamName = 'Name'                   #self represents the instance of the class and the variables of a class can be accessed using self
        self.TeamOrigin = 'Origin'               #set an attribute 'TeamOrigin to "Origin"

    '''
    DefinieTeamName and DefineTeamOrigin represents the methods of a class. Each method takes one
    arguments
    '''
    def DefineTeamName(self, Name):
        self.TeamName = Name

    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin

Team1 = Team()                                  #create an object of a class Team
'''
Methods and Member of a class can be accessed using a dot operator.
object.membername or object.methodname
'''
print(Team1.TeamName)                           #Access the member of a class using dot operator and print the value of a member
Team1.DefineTeamName("Tigers")                  #call methods of a class using a dot operator
print(Team1.TeamName)                           #print the value of a member TeamName
print(Team1.TeamOrigin)                         #print the value of a member TeamOrigin
Team1.DefineTeamOrigin("Chicago")               #call method DefineTeamOrigin of a class Team
print(Team1.TeamOrigin)                         #print value of a member TeamOrigin

'''
Again Define a class Team
'''
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

Team1 = Team("Tigers", "Chicago")                                   #creating an object of a class Team.
Team2 = Team("Hawks", "Newyork")                                    #creating an instance of a class Team and passing two values.
Team3 = Team()                                                      #creating an object of a class with no values passed.
print(Team1.TeamName)                                               #member can be accessed from outside the class using dot operator
Team1.DefineTeamName("Tigers")                                      #call methods from outside the class
print(Team1.TeamName)                                               #print the value of member TeamName
print(Team1.TeamOrigin)                                             #print the value of member TeamOrigin
Team1.DefineTeamOrigin("Chicago")                                  #call method DefineTeamOrigin
print(Team1.TeamOrigin)                                             #print the value of member
print(Team2.TeamName)                                              #print the value of member TeamName of object Team2
print(Team2.TeamOrigin)                                           #print the value of member TeamOrigin of object Team2
print(Team3.TeamName)                                               #print the value of member TeamName of object Team3
print(Team3.TeamOrigin)                                           #print the value of member TeamOrigin of object Team3
