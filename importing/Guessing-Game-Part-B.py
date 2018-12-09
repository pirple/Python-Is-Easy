##
# Guessing Game, Part B Lecture
##

# _*_ coding: utf-8 _*_

# import 'random' fuction of 'random' library
from random import random

# import 'clock' function of 'time' library
from time import clock

# Set the value of variable 'randVal' as a random number
randVal = random() # 0.0 <=N <1.0
## print(randVal)
## time.clock() -> timevalue
## time.clock() -> timevalue2

# Set the values of upper and lower as 1.0 and 0.0 respectively
upper = 1.0
lower = 0.0
## guess = 0.5 -> Too Low -> lower = 0.5
## guess = 0.9 -> Too High -> upper = 0.9
## guess = 0.5

# Set the variable 'startTime' as the currect processor time
startTime = clock()
while(True):
    # set the variable 'guess' as the avarage of 'upper' and 'lower'
    guess = (upper+lower)/2
    # check if 'guess' and 'randVal' are equal
    if guess == randVal:
        # get out of the loop if they are equal
        break
    # check if 'guess' is less than 'randVal'
    elif guess<randVal:
        lower = guess
    # check if 'guess' is more than 'randVal'
    else :
        upper = guess

# Set the variable 'endTime' as the currect processor time
endTime = clock()

# print the 'guess'
print(guess)

# print the time it took to run the loop
print('It took us:', endTime-startTime,'seconds')
