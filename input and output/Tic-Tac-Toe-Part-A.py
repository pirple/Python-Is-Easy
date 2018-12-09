##
# Tic Tac Toe, Part A Lecture
##

# _*_ coding: utf-8 _*_

"""
# The game should be similar to
# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
"""

#!python3

# Define a function
def drawField():
    for row in range(5):  #0,1,2,3,4
        # if row is even row write " | |  "
        if row%2 == 0:
            # print writing lines
            for column in range(5):  # will take values 0,1,2,3,4
                # if column is even, we will print a space
                if column%2 == 0:
                    if column != 4:
                        print(" ",end="") # Continue in the same line
                    else:
                        print(" ") # Jump to the next line
                else:
                    print("|",end="")
        else:
            print("-----")

"""
# We need to do the following
1. Apply and Save the move
2. Check which player turn is "X" or "O"
"""

# Create a variable for the Players
Player = 1
# Create a list with each element corresponds to a column
# currentField = [element1, element2, element3]
# Let's simulate our playing field
# In the first time, each list that correpond to a column will contains 3 empty spaces for the rows
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # A list that contains 3 lists


# Create an infinite loop for the gamez
while(True): # True == True / is always true (We can also use while(1))
    # Display the player's turn
    print("Players turn: ",Player)
    # Ask user for input: to specify the desired row and column
    MoveRow = int(input("Please enter the row\n"))       # Convert the row to integer
    MoveColumn = int(input("Please enter the column\n")) # Convert the column to integer
    if Player == 1:
        # Make move for player 1
        # Access our current field
        currentField[MoveColumn][MoveRow] = "X"
        # Once Player 1 make his move we change the Player to 2
        Player = 2
    else:
        # Make move for player 2
        currentField[MoveColumn][MoveRow] = "O"
        Player = 1
    # At the end, print the current field
    print(currentField)
