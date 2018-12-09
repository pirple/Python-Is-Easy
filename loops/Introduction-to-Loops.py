##
# Introduction to Loops Lecture
##

# -*- coding: utf-8 -*-



Word = "Hello"                       #initialize a variable Word with string "Hello"
Letters = []                         #create an empty list
'''
loop through each character of a string, print each character. Check if the character
in a string matches e, print a string and then append it into List
'''
for w in Word:                       #loop over each character
    print(w)                         #print a character
    if w == "e":                     #check if a character matches 'e'
        print("What a funny letter")
    Letters.append(w)                #Append each character into List.
print(Letters)                       #print the list
'''
Loop through each character stored in list Letters and then print each character
'''
for l in Letters:                    #Print each character in the list named Letters
    print(l)

'''
Create a list of 5 elements. Loop through each element in the list and print it.
'''
Numbers = [1, 2, 3, 4, 5]          #creating a list named Numbers with 5 integer elements
for l in Numbers:                  #loop over each element in list using for loop
    print(l)                       #print each element

'''
print all the numbers which has a remainder of zero when divisible by 2.
'''
for l in Numbers:                   #loop over all elements in the list
    if l%2 == 0:                    #check if remainder is 0 when divided by 2
        print(l)                    #print the number
'''
print all the numbers which has a remainder of one when divisible by 2.
'''
for l in Numbers:                   #loop over all elements in the list
    if l%2 == 1:                    #check if remainder is 1 when divided by 2
        print(l)                    #print the number

Numbers = []                        #create an empty list
for num in range(10):               #loop over elements from 0 to 9
    Numbers.append(num)             #append each number to List
    print(num)                      #print each number
print(Numbers)                     #print the list.

'''
Above process is repeated with value changed to 100. It prints all numbers from 0 to 99 and are appended
in list Numbers.
'''
Numbers = []                      #create an empty list
for num in range(100):            #loop over elements from 0 to 9
    Numbers.append(num)           #append each number to List
    print(num)                    #print each number
print(Numbers)                    #print the list

'''
range is a function which takes an integer as an input.
range(1, 10, 2): 1 is the start, 10 is end and 2 is the step size
'''
Numbers = []                      #create an empty list
for num in range(1, 10, 2):       #loop over an elements from 1 to 10 with difference of 2
    Numbers.append(num)           #append each number to List
    print(num)                    #print each number
print(Numbers)                    #print the list

Numbers = []                      #create an empty list
for num in range(-1, -12, -2):    #loop over an elements from -1 to -12 with difference of -2
    Numbers.append(num)           #append each number to List
    print(num)                    #print each number
print(Numbers)                    #print list

'''
Above example is repeated with a range now changed  from -1 to -13 at a difference of 3.
'''
Numbers = []
for num in range(-1, -13, 3):
    Numbers.append(num)
    print(num)
print(Numbers)
