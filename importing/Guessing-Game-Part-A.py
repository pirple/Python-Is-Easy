##
# Guessing Game, Part A Lecture
##

# _*_ coding: utf-8 _*_

# import the fuction 'randint' from library random
from random import randint

## randint(a,b) -> a<=N<=b

# set the variable 'randVal' with a random value between 0 to 100
randVal = randint(0,100)


while(True):
    guess = int(input('Please enter your guess:'))
    # check if 'guess' and 'randVal' are equal
    if guess == randVal:
        # get out of the loop if they are equal
        break
    # check if 'guess' is less than 'randVal'
    elif guess < randVal:
        print('Your guess was too low')
    # check if 'guess' is more than 'randVal'
    else:
        print('Too high')

# print the correct answer
print('You guessed correctly with:',guess)
