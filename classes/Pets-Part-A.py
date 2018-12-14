##
# Pets, Part A Lecture
##

# -*- coding: utf-8 -*-

# Define a class
class Pet:

  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,n,a,h,p):
    # Define an attribute and assign the value of the n argument
    self.name = n
    # Define an attribute and assign the value of the a argument
    self.age = a
    # Define an attribute and assign the value of the h argument
    self.hunger = h
    # Define an attribute and assign the value of the p argument
    self.playful = p

# Define a class
class Pet:

  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,name,a,h,p):
    # Define an attribute and assign the value of the name argument
    self.name = name
    # Define an attribute and assign the value of the a argument
    self.age = a
    # Define an attribute and assign the value of the h argument
    self.hunger = h
    # Define an attribute and assign the value of the p argument
    self.playful = p

  # getters
  # Define a function to return an attribute of the class
  def getName(self):
    # The function will return the name attribute
    return self.name

  # setters
  # Define a function which assigns a value to an attribute of the class
  def setName(self,name):
    self.name = name

# Define a class
class Pet:

  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,name,a,h,p):
    # Define an attribute and assign the value of the name argument
    self.name = name
    # Define an attribute and assign the value of the a argument
    self.age = a
    # Define an attribute and assign the value of the h argument
    self.hunger = h
    # Define an attribute and assign the value of the p argument
    self.playful = p

  # getters
  # Define a function to return an attribute of the class
  def getName(self):
    # The function will return the name attribute
    return self.name

  # setters
  # Define a function which assigns a value to an attribute of the class
  def setName(self,x):
    self.name = x


# Define a class
class Pet:

  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,name,a,h,p):
    # Define an attribute and assign the value of the name argument
    self.name = name
    # Define an attribute and assign the value of the a argument
    self.age = a
    # Define an attribute and assign the value of the h argument
    self.hunger = h
    # Define an attribute and assign the value of the p argument
    self.playful = p

  # getters
  # Define a function to return an attribute of the class
  def getName(self):
    # The function will return the name attribute
    return self.name

  # Define a function to return an attribute of the class
  def getAge(self):
    # The function will return the age attribute
    return self.age

  # Define a function to return an attribute of the class
  def getHunger(self):
    # The function will return the hunger attribute
    return self.hunger

  # Define a function to return an attribute of the class
  def getPlayful(self):
    # The function will return the playful attribute
    return self.playful

  # setters
  # Define a function which assigns a value to an attribute of the class
  def setName(self,xname):
    self.name = xname

  # Define a function which assigns a value to an attribute of the class
  def setAge(self,Age):
    self.age = Age

  # Define a function which assigns a value to an attribute of the class
  def setHunger(self,hunger):
    self.hunger = hunger

  # Define a function which assigns a value to an attribute of the class
  def setPlayful(self,play):
    self.playful = play

# Create an instance of the Pet class and assign values to the attributes
Pet1 = Pet("Jim",3,False,True)

# Print the value returned by the getName() function of the Pet1 instance
# This will print "Jim"
print(Pet1.getName())
#Print the value returned by the getPlayful() function of the Pet1 instance
# This will print True
print(Pet1.getPlayful())

# Call the setName(xname) function of the Pet1 instance
# This will assign a new value to the name attribute of the Pet1 instance
Pet1.setName("Snowball")
# Print the value returned by the getName() function of the Pet1 instance
# This will print "Snowball"
print(Pet1.getName())

# Access and print the name attribute of the Pet1 instance
# This will print "Snowball"
print(Pet1.name)

# Assign the value "Jim" to the name attribute of the Pet1 instance
Pet1.name = "Jim"
# Access and print the name attribute of the Pet1 instance
# This will print "Jim"
print(Pet1.name)
