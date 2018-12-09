##
# Nested Loops Lecture
##

# -*- coding: utf-8 -*-


# | |
#-----
# | |
#-----
# | |
'''
for loop
'''
for row in range(5):               #loop 5 times
    if row%2 == 0:                 #if remainder is equal to zero when divided by 2
        print(" | | ")             #print message
    else:                          #if above condition is false
        print("-----")             #print message

'''
 | |
-----
 | |
-----
 | |
printing the above shapes
'''
for row in range(5):              #loop 5 times
    if row%2 == 0:                #if remainder is equal to zero when divided by 2
        for column in range(1, 6): #created a nested loop of range from 1 to 6
            if column%2 == 1:      #check if remainder is 1 when divided by 2
                if column != 5:    #if variable column not equal to 5
                    print(" ", end = "")   #print space and in the same line
                else:
                    print(" ")     #print in next line
            else:
                print("|", end = "") #print a pipe in  same line

    else:
        print("-----")               #print dash
