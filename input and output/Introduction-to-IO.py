##
# Introduction to Input and Output Lecture
##

# _*_ coding: utf-8 _*_


# Display a message to the user to write an input that will be saved into the Var variable
Var = input("Message to the user")

Name = input("Please to enter your name: ")
# Read back the name
print(Name)

# All inputs are going to be imported as strings
Age = input("Please enter your age: ")
# Print out the Age
print(Age)

# However, we cannot print the Age + 1 for example since Age is a string (ie: "21"+1)
#print(Age+1)
# For example: this will work
print("21"+"1") # Gives 211
# Or in case both of them are integers
print(21+1)

# So we need to convert our input to an integer
# But note that you can not put caracters like "twenty one"
Age = int(input("Please enter your age: ")) # Age here will be an integer
# The following instruction becames valid for now
print(Age+1)
# Again, this is not valid because we are trying to add an integer(Age) to a string("1")
#print(Age+"1")
# We can for now convert both of the inputs to strings
print(str(Age)+"1") # str(Age) = str(21) -> "21"
# Age = 21

# Another method is to convert the Age later
Age = input("Please enter your age: ") # Age here will be an integer
# The following instruction becames valid for now
print(int(Age)+1) # This will temporary convert Age string to integer


# Create an empty list
Scores = []
# Ask the user for 5 different scores using a loop
for i in range(5):   # Create a range , variable i will start by value 0 to 4 at the end of the loop ([0,4[)
    # currentScore = int(input("Please enter the score: "))
    # Or we can also print which score to put: but accept only integers
    # currentScore = int(input("Please enter the score " + str(i+1) + ": ")) # Add 1 because i will start by 0
    # We can also convert it to float so also decimals could be taken into account
    currentScore = float(input("Please enter the score " + str(i+1) + ": "))
    # Append the score to our list (at the end) using the predefined function : append
    Scores.append(currentScore)
    # Print the score entered by the user, we use comma to format our variable to string automatically
    # print("The score you entered was: ",currentScore)
    # We can put something else afterwards
    # print("The score you entered was: ",currentScore, "nice")
    # We can use "\n" to put our score in a new line: "\" is used to mention a special caracter
    # print("The score you entered was:\n",currentScore)
    # To convert our score to an integer
    print("The score you entered was: \n"+str(currentScore))

# print is actually a function that takes those inputs separated by "," and prints them
# def FunctionName(input1,input2):
#       Action


# What happens inside our loop ? (Below an example for integers)
#   Scores = []
#   Scores = [70]                   # First loop i = 0
#   Scores = [70, 12]               # First loop i = 1
#   Scores = [70, 12, 45]           # First loop i = 2
#   Scores = [70, 12, 45, 56]       # First loop i = 3
#   Scores = [70, 12, 45, 56, 99]   # First loop i = 4

# Print the list Scores
print(Scores)
