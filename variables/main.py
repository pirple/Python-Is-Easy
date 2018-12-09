##
# Variables Lecture
##

# -*- coding: utf-8 -*-


# 'one' is the name of the variable
# '=' is called the assignment operator we use to store values in a variable
# '1' is the actual value stored inside the variable 'one'
one = 1

# 'two' is the name of the variable
# '=' is called the assignment operator we use to store values in a variable
# '2' is the actual value stored inside the variable 'two'
two = 2

# 'three' is the name of the variable
# '=' is called the assignment operator we use to store values in a variable
# '3' is the actual value stored inside the variable 'three'
three = 3

# 'print()' is a function we use in python to print some value or content on the screen
# name of the variable can be passed inside the print function to display its value on screen
print(one)
print(two)
print(three)
print(two)
print(one)
# The above code will print the following
# Notice how the same variable is being used again for printing
"""
1
2
3
2
1
"""



print(one)
print(two)
print(three)
# the value of a variable can be overwritten again by using the assignment operator '=' to store a new unique value
two = 4
print(two)
print(one)
# The above code will print the following
# Notice the value of variable 'two' is reassigned to '4' in the output
"""
1
2
3
4
1
"""

# apart from storing integer values , decimal values can also be stored inside a variable
# notice how the decimal value '1.1' is stored inside a variable called 'decimal'
decimal = 1.1
# The above code will print the following
"""
1.1
"""


# text values also called strings can be stored inside a variable
# notice how the value 'Hello' is stored inside a variable 'StringVar'
StringVar = "Hello"
# The above code will print the following
"""
Hello
"""

# will produce and error with the following message
"""
StringVar = "Hello" + 1
TypeError: must be str, not int
"""
# uncomment this code execute the script to see error
#StringVar = "Hello" + 1
# this happens because variables cant be of two types of 'int' denotes to integer and 'str' denotes to string


StringVar = "Hello" + "1"
# The above code will print the following
# The above code works beause now both 1 and hello are strings
"""
Hello1
"""

# The def keyword is used to begin fuction declaration and then the name of function is wriiten
def FunctionName():
    # Declaring local variable
    newVar="World"
    # Printing local variable
    print(newVar)
    # Used to indicate global variable is used
    global one
    # Printing global one variable
    print(one)
    # Returing a value , also used for ending a function
    return

# The function being called by using its name along with ()
FunctionName()
# Printing a local variable
print(newVar)
# The following error is produced with due to the fact that 'newVar is a local variable'
"""
NameError: name 'newVar' is not defined
"""

# Shorthand way of declaration variables
one , two , three = 1,2,3
print(one)
print(two)
print(three)
# The above code will print the following
"""
1
2
3
"""

# Declaraing a variable and storing the value 5 into it
Five = 3+2
print(Five)
# The above code will print the following
"""
5
"""

# Will produce error because we cant add two variables with one value on the right of assignment operator
Five + Six = 3+2

# This will produce an error as well
# left = what you're giving the value to
# right = what the value is
5 = Five
# Trying to print the value of variable 'Five'
print(Five)

# Declared a variable 'count' and stored the value 0 to it
count = 0
# Printing count value
print(count)
# Output
"""
0
"""

# Reassign the value of count to 1
count = 1
# Printing count value
print(count)
# Output
"""
1
"""


# This will also increase the count value by adding 1 to the previous value of count
count = count + 1
# Printing count value
print(count)
# Output
"""
2
"""
# This will also increase the count value by adding 1 to the previous value of count
count = count + 1
# Printing count value
print(count)
# Output
"""
3
"""

# This will also increase the count value by adding 1 to the previous value of count
# Short hand notation of the same line as 'count=count+1'
count+=1
# Printing count value
print(count)
# Output
"""
4
"""

# Assign 0 value to variable count
count = 0
# Print the value
print(count)
# Incrementing count value
count = count + 1
# Print the value
print(count)
# Multiply the value of count by 3
count*=3
# Print the value
print(count)
# Output
"""
0
1
3
"""

# Assign 0 value to variable count
count = 0
# Print the value
print(count)
# Incrementing count value
count = count + 1
# Print the value
print(count)
# Multiply the value of count by 3
count/=3
# Print the value
print(count)
# Output
"""
0
1
0.333333333333
"""
