##
# Introduction to Importing Lecture
##

# _*_ coding: utf-8 _*_

# Importing the library 'random' as 'r' where 'r' is its nickname
import random as r

# Assign a random integer value to the variable 'randInt'
# random.seed(1)
randInt = r.randint(0,10) #start<=N<=end
print(randInt)

# Assign a random float value to the variable 'randFloat' between 0 and 1 only
randFloat = r.random() #0.0<=N<1.0
print(randFloat)

# Assign a random float value to the variable 'randFloat' between any specified range
randUniform = r.uniform(1,11) #start<=N<=end
print(randUniform)
