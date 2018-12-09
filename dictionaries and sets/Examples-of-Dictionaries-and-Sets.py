##
# Examples of Dictionaries and Sets - Lecture
##


# Declaring a dictonary variable named 'BlackShoes' and assigning keys and values to it
# 42 , 41, 40 , 39 , 38 are the keys
# 2 , 3 , 4 , 1 , 0 are the corresponding values
BlackShoes={42:2,41:3,40:4,39:1,38:0}

# Printing the dictionary variable 'BlackShoes'
print(BlackShoes)

# Using a while loop which will run endlesly until a given condition is met
while (True): # True==True
    # Taking input from user and assigning it to variable named 'purchaseSize' using 'input()' function
    # notice \n in the code which is used to bring new line
    # int(variable_name) converts the the variable to type integer
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    # Accessing the value of key 'purchaseSize' and decreasing it by 1
    BlackShoes[purchaseSize] -= 1 # BlackShoes[purchaseSize]=BlackShoes[purchaseSize]-1 both are same
    # Printing the dictionary variable 'BlackShoes'
    print(BlackShoes)
# Output
"""
{42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?
42
{42: 1, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?
39
{42: 1, 41: 3, 40: 4, 39: 0, 38: 0}
Which shoe size would you like to buy?
38
{42: 1, 41: 3, 40: 4, 39: 0, 38: -1}
"""
# Notice the issue in the code where the value of shoe size goes to negative and this needs to be fixed



# Declaring a dictonary variable named 'BlackShoes' and assigning keys and values to it
# 42 , 41, 40 , 39 , 38 are the keys
# 2 , 3 , 4 , 1 , 0 are the corresponding values
BlackShoes={42:2,41:3,40:4,39:1,38:0}

# Printing the dictionary variable 'BlackShoes'
print(BlackShoes)

# Using a while loop which will run endlesly until a given condition is met
while (True): # True==True
    # Taking input from user and assigning it to variable named 'purchaseSize' using 'input()' function
    # notice \n in the code which is used to bring new line
    # int(variable_name) converts the the variable to type integer
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    # If statement is used in order to check if the value of shoe size is greater than zero
    if BlackShoes[purchaseSize] > 0:
        # Accessing the value of key 'purchaseSize' and decreasing it by 1
        BlackShoes[purchaseSize] -= 1 # BlackShoes[purchaseSize]=BlackShoes[purchaseSize]-1 both are same
    # If size is not greater than zero then we print message using 'print()' function to user
    else:
        # Printing message
        print("Shoes are no longer in stock")
    # Printing the dictionary variable 'BlackShoes'
    print(BlackShoes)
# Output
"""
{42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?
42
{42: 1, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?
38
Shoes are no longer in stock
{42: 1, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?

"""
# Notice that the negative number problem is fixed but the loop is never ending and this needs to be fixed as well




# Declaring a dictonary variable named 'BlackShoes' and assigning keys and values to it
# 42 , 41, 40 , 39 , 38 are the keys
# 2 , 3 , 4 , 1 , 0 are the corresponding values
BlackShoes={42:2,41:3,40:4,39:1,38:0}

# Printing the dictionary variable 'BlackShoes'
print(BlackShoes)

# Using a while loop which will run endlesly until a given condition is met
while (True): # True==True
    # Taking input from user and assigning it to variable named 'purchaseSize' using 'input()' function
    # notice \n in the code which is used to bring new line
    # int(variable_name) converts the the variable to type integer
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    # If statement is used to check if the entered amount is less than 0
    if purchaseSize < 0:
        # if it is then 'break' keyword is used to terminate the loop
        break
    # If statement is used in order to check if the value of shoe size is greater than zero
    if BlackShoes[purchaseSize] > 0:
        # Accessing the value of key 'purchaseSize' and decreasing it by 1
        BlackShoes[purchaseSize] -= 1 # BlackShoes[purchaseSize]=BlackShoes[purchaseSize]-1 both are same
    # If size is not greater than zero then we print message using 'print()' function to user
    else:
        # Printing message
        print("Shoes are no longer in stock")
    # Printing the dictionary variable 'BlackShoes'
    print(BlackShoes)
# Output
"""
{42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?
38
Shoes are no longer in stock
{42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
Which shoe size would you like to buy?
40
{42: 2, 41: 3, 40: 3, 39: 1, 38: 0}
Which shoe size would you like to buy?
-1
"""
