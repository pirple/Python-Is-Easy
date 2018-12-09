##
# Making Shapes With Loops Lecture
##

# -*- coding: utf-8 -*-

Length = 10                  #set a variable name Length = 10
'''
On each loop character c is printed n number of times which is defined by pos.
"c"*2 means character c is repeated twice
'''
for pos in range(1, 10):     #loop from 1 to 9
    print("c"*pos)           #print character c

Length = 10                   #set a variable name Length = 10
ToPrint = "a"                 #a variable name ToPrint is assigned a character "a"
for pos in range(1, Length + 1): #loop from 1 to value of Length + 1
    print(ToPrint*pos)         #print character n number of times

'''
Loop in a decreasing order from 10 to 0 and print a character n times on each decreasing loop
'''
for pos in range(Length, 0, -1):
    print(ToPrint*pos)
'''
Loop in a increasing order from 1 to 12 and print a character n times on each increasing loop
'''
Length = 12
ToPrint = "1"                  #a variable name ToPrint is assigned a character "1"
for pos in range(1, Length + 1):
    print(ToPrint*pos)
'''
Loop in a decreasing order from 12 to 0 and print a character "1" n times on each decreasing loop
'''
for pos in range(Length, 0, -1):
    print(ToPrint*pos)
