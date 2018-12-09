##
# Lists Lecture
##

# -*- coding: utf-8 -*-


TestList = ["element1", "element2", "element3"]             #TestList is a list with three elements
#Scores is a list with different data types
Scores = [70, 85, 67.5, 90, 80]
print(Scores)                                                #print Scores list
'''
elements of a list can be accessed with a index inside a square bracket
Accessing list elements. The first element of a list starts from 0
'''
print(Scores[0])                               #prints 1st element of a list
print(Scores[1])                               #prints 2nd element of a list
print(Scores[2])                               #prints 3rd element of a list
print(Scores[3])                               #prints 4th element of a list
print(Scores[4])                               #prints 5th element of a list
'''
Accessing list in a reverse order
'''
print(Scores[-1])                              #prints last element of a list
print(Scores[-2])                              #prints 2nd last element of a list
print(Scores[-3])                              #prints 3rd last element of a list
print(Scores[-4])                              #prints 4th last element of a list
print(Scores[-5])                              #prints 5th last element of a list
'''
Accessing multiple elements from a list.
It can be done using List[first : last]
'''
print(Scores[0:2])                             #access elements from index 0 to index 1
print(Scores[0:3])                             #access elements from index 0 to index 2
print(Scores[1:3])                             #access elements from index 1 to index 2
print(Scores[2:])                              #access all elements from index 2 to end
print(Scores[1:])                              #access all elements from index 1 to end

'''
Values of a list can be changed
'''
Scores = [70, 85, 67.5, 90, 80]                #initialize list with values
print(Scores)                                  #print a list named Scores
Scores[0] = 75                                 #assign a value of 75 to the first element of a list Scores
print(Scores)                                  #print the Scores
Scores = [70, 85, 67.5, 90, 80]                #initialize list with values
Scores[0] = 6.0                                #assign a float value 6.0 to the first element of a list
print(Scores)                                  #print Scores
Scores = [70, 85, 67.5, 90, 80]                #initialize list with values
print(Scores)                                  #print Scores
Scores[0] = "Hello"                            #assign a string 'Hello' to the first element of a list
print(Scores)                                  #print Scores
Scores = [70, 85, 67.5, 90, 80]                #initialize list with values
print(Scores)                                 #print Scores
Scores[1:3] = []                               #remove elements 2nd to 3rd from the list
print(Scores)                                 #print Scores
Scores = [70, 85, 67.5, 90, 80]               #initialize list with values
print(Scores)                                 #print Scores
Scores[2:3] = []                              #remove 3rd element from the list.
print(Scores)                                 #print Scores list
Scores = [70, 85, 67.5, 90, 80]               #initialize list with values
print(Scores)                                 #print Scores list
Scores[2] = []                                #assign an empty list to element 3rd (index 2nd)
print(Scores)                                 #print Scores
Scores = [70, 85, 67.5, 90, 80]               #initialize list with values
print(Scores)                                 #print Scores
Scores[2] = ["Hello", "World"]                #assign a list to 3rd element (index 2nd)
print(Scores)                                 #print Scores
print(Scores[2])                              #accessing the 3rd element
'''
Accessing list within a list
'''
print(Scores[2][0])                           #access the list within a list
print(Scores[2][1])
Scores = [70, 85, 67.5, 90, 80]              #initialize list with values
print(Scores)                                #print Scores
Scores.append(82)                            #appending value at the end of list
print(Scores)                                #print Scores
