##
# Tic Tac Toe, Part B Lecture
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

# Define the function drawField that will print the game field
# We will try to put our current field into the draw field

def drawField(field):
    for row in range(5):  #0,1,2,3,4
                          #0,.,1,.,2
        # if row is even row write " | |  "
        if row%2 == 0:
            practicalRow = int(row/2)
            # print writing lines
            # In this case , we have to adapt our field (3*3) to the actual drawing (5*5)
            # We can divde by 2 to get the correct maping
            for column in range(5):  # will take values 0 (in drawing) -> 0 (in actual field), 1->., 2->1, 3->., 4->2
                # if column is even, we will print a space
                # The even columns gives us the move of each player
                if column%2 == 0: # Values 0,2,4
                    # The actual column that should be used in our field
                    # Make sure our values are integers
                    practicalColumn = int(column/2)  # Values 0,1,2
                    if column != 4:
                        # Print the specific field
                        print(field[practicalColumn][practicalRow],end="") # Continue in the same line
                    else:
                        print(field[practicalColumn][practicalRow]) # Jump to the next line
                else:
                    # The odd value just give us vertical lines
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

# We will draw the current field
drawField(currentField)

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
        # We only want to make one move when that specific field is empty
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            # Once Player 1 make his move we change the Player to 2
            Player = 2
    else:
        # Make move for player 2
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1

    # At the end, draw the current field representation
    drawField(currentField)
