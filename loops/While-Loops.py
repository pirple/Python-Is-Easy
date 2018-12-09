##
# While Loops Lecture
##

# -*- coding: utf-8 -*-

'''
While Loops
Syntax:
    while condition:
        Action1
        Action2
        ACtion3
'''
counter = 1                         #set counter variable equal to 1
'''
The while loop runs until the condition is True, updates the counter, prints the counter.
It comes out of the loop if the condition fails.
'''
while (counter <= 10):             #checks condition
    print(counter)                 #print value of counter
    counter = counter + 1          #increments counter by 1

counter = 1                       #sets counter variable equal to 1
Sum = 0                           #initialize sum to 0
while (counter <= 10):            #checks condition
    print(counter)                #print value of counter
    Sum = Sum + counter           #add sum and counter value
    counter = counter + 1          #increments counter by 1
print(Sum)                       #print the value of sum

'''
print the sum of values from 1 to 100
'''
counter = 1                     #set counter equal to 1
Sum = 0                         #intialize sum to 0
while (counter <= 100):         #check the value of counter until it is less than or equal to 100
    print(counter)              #print the value of counter
    Sum = Sum + counter         #add the sum and counter
    counter = counter + 1       #increment counter by 1
print(Sum)                      #print Sum

KeepTrack = 1
Sum = 0
while (KeepTrack <= 100):
    print(KeepTrack)
    Sum = Sum + KeepTrack
    KeepTrack = KeepTrack + 1
print(Sum)

Letters = ["a", "b", "c", "d", "e"]             #initialize a list with 5 character elements
Index = 0                                       #set index equal to 0
while (Index < len(Letters)):                 #Compare variable Index with length of list
    print(Index)                               #print value of Index
    print(Letters[Index])                     #print each element in a List
    Index = Index + 1                        #Increment value of Index by 1.

'''
Starts from Index 4. Since the length of list is equal to 5. the loop runs only once
and prints the last element only.
'''
Index = 4                      #set index equal to 4
while (Index < len(Letters)):   #Compare variable Index with length of list
    print(Index)                #print value of Index
    print(Letters[Index])       #print each element in a List
    Index = Index + 1           #Increment value of Index by 1.


'''
The code below does not print anything since the loop starts from 5 and condition does not meet.
'''
Index = 5
while (Index < len(Letters)):
    print(Index)
    print(Letters[Index])
    Index = Index + 1

height = 5000                   #set variable height equal to 5000.
velocity = 50                   #set variable velocity equal to 50
time = 0                        #set variable time equal to 0
while (height > 0):             #check if variable height > 0
    height = height - velocity  #decrement height with velocity and assign the value to height.
    time = time + 1            #increment time by value 1

print(height)                   #print value of height
print(time)                     #print value of time
