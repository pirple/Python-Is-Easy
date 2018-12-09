##
# Breaking and Continuing in Loops Lecture
##

# -*- coding: utf-8 -*-


Participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]              #create a list of 5 elements.

position = 0                                                      #set position is equal to 0
for name in Participants:                                         #loop over each element of list
    if name == "Tina":                                            #check if the element of list matches to "Tina"
        break                                                     #come outside of loop if the condition is met
    position = position + 1                                       #increment variable position by 1

print(position)                                                   #print the value of position

position = 0                                                   #set position is equal to 0
for name in Participants:                                      #loop over each element of list
    if name == "Tina":                                          #check if the element of list matches to "Tina"
        print("About to break")                               #print message
        break                                                   #come outside of loop if the condition is met
    print("About to increment")                                #print message
    position = position + 1                                   #increment variable position by 1

print(position)                                               #print the value of position

'''
finds the index of matched string from the list
'''
Index = 0                                           #set Index to 0
for currentIndex in range(len(Participants)):       #loop over all elements in list
    print(currentIndex)                             #print value of currentIndex
    if Participants[currentIndex] == "Joe":         #check if list element is equal to Joe
        print("Have Breaked")                       #print message
        break                                      #come out of the loop
    print("Not Breaked")                           #print message
print(currentIndex+1)                              #print currentIndex of matched element

for number in range(10):                           #loop from range of 0 to 10
    if number%3 == 0:                              #check remainder is 0 if divided by 3
        print(number)                              #print value of a number
        print("Divisible by 3")                    #print message
        continue                                    #continue
    print(number)                                  #print value of number
    print("Not Divisible by 3")                    #print message
