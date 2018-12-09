##
# Math Library Lecture
##

# _*_ coding: utf-8 _*_

# import the library 'math'
import math

# square root of the variable 'Val' using 'sqrt' function
Val = 3.14
sqrtVal = math.sqrt(Val)
print(sqrtVal) # sqrtVal**(2) = sqrtVal^2

# exponential value of the variable 'Val' using 'exp' function
expVal = math.exp(Val) #e^(Val)
print(expVal)

# factorial of the variable 'Val' using 'factorial' function and print it
factVal = math.factorial(math.floor(Val)) #5! = 5*4*3*2*1
print(factVal)

# sine value of the variable 'Val' using sin function and print it
sinVal = math.sin(Val)
print(sinVal)

# the nearest integer which is less than the value of 'Val' and print it
floorVal = math.floor(Val)
print(floorVal)

# the nearest integer which is greater than the value of 'Val' and print it
ceilingVal = math.ceil(Val)
print(ceilingVal)
