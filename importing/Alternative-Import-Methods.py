##
# Alternative Import Methods Lecture
##

# _*_ coding: utf-8 _*_

# Importing the library 'random' as 'r' where 'r' is its nickname
## from random import *
import random as r

# import the function from the library
## from random import randInt

# Assign a random integer value to the variable 'randInt'
## random.seed(1)
randInt = r.randint(0,10) #start<=N<=end
print(randInt)

# Assign a random float value to the variable 'randFloat' between 0 and 1 only
randFloat = r.random() #0.0<=N<1.0
print(randFloat)

# Assign a random float value to the variable 'randFloat' between any specified range
randUniform = r.uniform(1,1100) #start<=N<=end
print(randUniform)

# Create a list 'simpleList' and print a random integer from that list
simpleList = [1,3,5,7,11]
pickElement = r.choice(simpleList)
print(pickElement)
print(simpleList)

# shuffle the list using 'shuffle' function of 'random' library
r.shuffle(simpleList)
print(simpleList)
