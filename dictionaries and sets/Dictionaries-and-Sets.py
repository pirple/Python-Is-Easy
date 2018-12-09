##
# Dictionaries and Sets Lecture
##

# -*- coding: utf-8 -*-


"""
A set is a data structure in python like a list to store a variety of hetrogenous unique elements.
Hetrogenous means a set can contain primitive types  integer , string , float in it.
Unique means that each element can occur only once in a set
"""

# Declaring a set 'Sets' with different string values in it
Sets={"Element1","Element2","Element1","Element4"}
# Printing variable 'Sets' using the 'print' function
print(Sets)
# Output
"""
{'Element1', 'Element4', 'Element2'}
"""
# Notice how the output is different from the input in two ways
# 1) Only unique elements are printed
# 2) Elements are not printed in the same order as they were stored because in sets order doesnt matter


# Here 'if' condition is used along with 'in' keyword to check whether the value "Element1" is present in set 'Sets'
if "Element1" in Sets:
    # If the value "Element1" is found print "Yes" to console
    print("Yes")
# Output
"""
Yes
"""


# Declaring a list variable 'CountryList' and assigning empty list to it by using '[]'
CountryList = []

# For loop is used with 'range(5)' indicating the loop will run 5 times from 0-4
for i in range(5):
    # Taking input from user and assigning it to variable named 'Country' using 'input(range_value)' function
    Country = input("Please Enter Your Country: ")
    # 'append(variable_name)' function is used here which adds a new element into the list 'CountryList'
    CountryList.append(Country)

# A new set 'CountrySet' is created using the 'set(variable_name)' function by passing the variable 'CountryList' which will convert the 'CountryList' to a set
CountrySet = set(CountryList)

# Printing list 'CountryList'
print(CountryList)
# Printing set 'CountrySet'
print(CountrySet)
# Output
"""
Please Enter Your Country: US
Please Enter Your Country: France
Please Enter Your Country: India
Please Enter Your Country: Brazil
Please Enter Your Country: France
['US', 'France', 'India', 'Brazil', 'France']
{'France', 'India', 'Brazil', 'US'}
"""
# First the program asks to entry country names 5 times and then the list and set is printed
# Notice how the set has changed order and only prints unique elements which is the property of set

# Here 'if' condition is used along with 'in' keyword to check whether the value "Brazil" is present in set 'CountrySet'
if "Brazil" in CountrySet:
    # If the value "Brazil" is found print "attended" to console
    print("attended")
# Output
"""
attended
"""

"""
A dictionary is another data structure in python that also supports hetrogenous data to be stored inside it.
Rather than using index like used in list , a dictionary supports key-value structure where the key is used like an index and value is stored besides it like how values are stored in a variable
A dictionary should also contain unique keys and can contain even lists inside of it.
"""

# Declaring a dictonary variable named 'Dictonary' and assigning keys and values to it
# "Key" , "Key1", "Key2" are the keys
# "Value" , "Value1" , "Value2" are the corresponding values
Dictionary={"Key":"Value","Key1":"Value1","Key2":"Value2"}
# Printing the dictonary variable 'Dictionary'
print(Dictionary)
# Output
"""
{'Key': 'Value', 'Key1': 'Value1', 'Key2': 'Value2'}
"""


# Declaring a list variable 'CountryList' and assigning empty list to it by using '[]'
CountryList = []

# For loop is used with 'range(5)' indicating the loop will run 5 times from 0-4
for i in range(5):
    # Taking input from user and assigning it to variable named 'Country' using 'input(range_value)' function
    Country = input("Please Enter Your Country: ")
    # 'append(variable_name)' function is used here which adds a new element into the list 'CountryList'
    CountryList.append(Country)


# Declaring a dictionary variable 'CountryDictionary' and assigning empty dictionary to it by using '{}'
CountryDictionary={}

# A for loop is used using 'for in syntax' to access the elements of list 'CountryList' and stored it in local variable named 'Country'
for Country in CountryList:
    # If statement is used in order to check if the country name is present as a key in dictionary 'CountryDictionary'
    if Country in CountryDictionary:
        # upon finding the key the value is accessed using 'DictionaryName[key_name]' synatx and incremented one to it
        CountryDictionary[Country] +=1
    else:
        # if the key is not found then creating a new key with country name and assigning one to it
        # Notice how no error will be produced which was occuring in list when tried to access an element whcih didnt existed
        CountryDictionary[Country] = 1

# Printing the dictionary variable 'CountryDictionary'
print(CountryDictionary)
# Output
"""
Please Enter Your Country: US
Please Enter Your Country: France
Please Enter Your Country: India
Please Enter Your Country: Brazil
Please Enter Your Country: France
{'France': 2, 'India': 1, 'Brazil': 1,'US': 1}
"""
# No order is mainatined in dictionary as well
