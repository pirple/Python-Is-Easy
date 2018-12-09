##
# Functions Lecture
##

# -*- coding: utf-8 -*-

# Assignment on Functions
'''
Syntax for a function:

def FunctionName(Input):
    Action
    return Output
'''
# define a function using a keyword def
'''
function name: addOne
input: Number
output: Output
'''
#The function addOne takes a Number as input and then adds 1 and then returns it
def addOne(Number):
    Output = Number + 1                      #add 1 to a Number
    return Output                            #return output

Var = 0                                     #intialize to 0
print(Var)                                  #print value
'''
an argument is passed through a function.
'''
Var2 = addOne(Var)                          #calling a function addOne and is assigned to a variable
Var3 = addOne(Var2)                         #calling a function addOne and is assigned to a variable
Var4 = addOne(2)                            #a value is directly passed through a function and the output is
                                            #assigned to a variable
#print Var2, Var3 and Var4
print(Var2)
print(Var3)
print(Var4)

Var4 = addOne(2.1)                         #float value is passed into a function
print(Var4)                                #print the value
Var4 = addOne(2.1+3.4)                     #two float numbers are added and passed into a function
print(Var4)                                #print the value

'''
function addOneAddTwo takes two variable as an input and then returns a variable.
'''
def addOneAddTwo(NumberOne, NumberTwo):
    Output = NumberOne + 1                #add 1 to a variable NumberOne
#    Output = Output + NumberTwo + 2
    Output += NumberTwo + 2               #add 2, NumberTwo variable and Output
    return Output                         #return Output variable

Sum = addOneAddTwo(1, 2)                 #call the function addOneTwo and pass two arguments directly
print(Sum)                               #print output
Sum = addOneAddTwo(Var2, Var3)           #call the function addOneTwo and pass two variable arguments
print(Sum)                               #print output
