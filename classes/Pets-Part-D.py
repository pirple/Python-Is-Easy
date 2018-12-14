##
# Pets, Part D Lecture
##

# -*- coding: utf-8 -*-


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

  # Define a function which refers to the class and returns a string
  def __str__(self):
     # Define the string which the function returns
    return (self.name + " is " +str(self.age) + " years old")


# The class is commented becuse two errors exist. One is in line 65 where the self argument is missing
# and the second error is in line 81 where the code should be self.FavoriteToy
# Define a class which inherits the Pet class
#class Dog(Pet):
#
#  # Define a function which refers to the class in order to initiliaze the attributes of the class
#  def __init__(self,name,age,hunger,playful,breed,FavoriteToy):
#    # Call the initializer of the parent class with the proper parameters
#    # Error - the self argument is missing
#    Pet.__init__(name,age,hunger,playful)
#
#    # The following line will return an error if uncommented
#    #self.__init__(name,age,hunger,playful)
#
#    # Define an attribute and assign the value "None"
#   self.breed = breed
#    self.FavoriteToy = FavoriteToy
#
#  # Define unction which refers to the class
#  def wantsToPlay(self):
#
#    # IF condition is True
#    if self.playful == True:
#      # Define the string which the function returns
#      # Error - It should be self.FavoriteToy
#      return("Dog wants to play with " + FavoriteToy)
#
#    # ELSE condition
#    else:
#      # Define the string which the function returns
#      return("Dog doesn't want to play")
#
# Create an instance of the Dog class and assign values to the attributes
#huskyDog = Dog("Snowball",5,False,True,"Husky","Stick")
#
# Assign to a variable the result returned by the wantsToPlay() function of the huskyDog instance
#Play = huskyDog.wantsToPlay()
#
# Print the value of the Play variable
# This will print "Dog wants to play with Stick"
#print(Play)



# Define a class which inherits the Pet class
class Dog(Pet):

  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,name,age,hunger,playful,breed,FavoriteToy):
    # Call the initializer of the parent class with the proper parameters
    Pet.__init__(self,name,age,hunger,playful)

    # The following line will return an error if uncommented
    #self.__init__(name,age,hunger,playful)

    # Define an attribute and assign the value of the breed argument
    self.breed = breed
    # Define an attribute and assign the value of the FavoriteToy argument
    self.FavoriteToy = FavoriteToy

  # Define unction which refers to the class
  def wantsToPlay(self):
    # IF condition is True
    if self.playful == True:
      # Define the string which the function returns
      return("Dog wants to play with " + self.FavoriteToy)
    # ELSE condition
    else:
      # Define the string which the function returns
      return("Dog doesn't want to play")


# Define a class which inherits the Pet class
class Cat(Pet):

  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,name,age,hunger,playful,place):

    # Call the initializer of the parent class with the proper parameters
    Pet.__init__(self,name,age,hunger,playful)

    # Define an attribute and assign the value of the place argument
    self.FavoritePlaceToSit = place

  # Define unction which refers to the class
  def wantsToSit(self):
    # IF condition is True
    if self.playful == False:
      # Define the string which the function prints
      # The following line will produce an error if uncommented due to the self.place part of the code
      #print("The cat wants to sit in" ,self.place)
      print("The cat wants to sit in" ,self.FavoritePlaceToSit)
    # ELSE condition
    else:
      # Define the string which the function prints
      print("The cat wants to play")

  # Define a function which refers to the class and returns a string
  def __str__(self):
    # Define the string which the function returns
    return (self.name + " likes to sit in " + self.FavoritePlaceToSit)

# Define a class
class Human:
  # Define a function which refers to the class in order to initiliaze the attributes of the class
  def __init__(self,name,Pets):
    # Define an attribute and assign the value of the name argument
    self.name = name
    # Define an attribute and assign the value of the Pets argument
    self.Pets = Pets

  def hasPets(self):
    # IF condition is True
    # If the Human has Pets
    if len(self.Pets) != 0:
      # Define the string which the function returns
      return "yes"
    # ELSE condition
    else:
      # Define the string which the function returns
      return "no"





# Create an instance of the Dog class and assign values to the attributes
huskyDog = Dog("Snowball",5,False,True,"Husky","Stick")

# Assign to a variable the result returned by the wantsToPlay() function of the huskyDog instance
Play = huskyDog.wantsToPlay()

# Print the value of the Play variable
# This will print "Dog wants to play with Stick"
print(Play)

# Assign the value False to the playful attribute of the huskyDog instance
huskyDog.playful = False

# Assign to a variable the result returned by the wantsToPlay() function of the huskyDog instance
Play = huskyDog.wantsToPlay()

# Print the value of the Play variable
# This will print "Dog doesn't want to play"
print(Play)

# Create an instance of the Cat class and assign values to the attributes
typicalCat = Cat("Fluffy",3,False,False,"the sun ray")

# Call the wantsToSit() function of the typicalCat instance
# This will print "The cat wants to sit in the sun ray"
typicalCat.wantsToSit()

# This will print the returned string from the __str__ function of the typicalCat instance
# This will print "Fluffy likes to sit in the sun ray"
print(typicalCat)
# The __str__ function is not defined in the Dog function so it will return general inforamtion on the class
# This will print <class '__main__.Dog'>
print(Dog)
# This will print the returned string from the __str__ function of the huskyDog instance which is inherited by the Pet class
# This will print "Snowball is 5 years old"
print(huskyDog)

# Create an instance of the Human class and assign values to the attributes
yourAverageHuman = Human("Alice",[huskyDog,typicalCat])

# Assign to a variable the result returned by the hasPets() function of the yourAverageHuman instance
hasPet = yourAverageHuman.hasPets()

# Print the value of the hasPet variable
# This will print "yes"
print(hasPet)

# Print the first element in the Pets list attribute of the yourAverageHuman instance
# The huskyDog instance is the first element in the Pets list attribute of the yourAverageHuman instance
# This will print the returned string from the __str__ function of the huskyDog instance which is inherited by the Pet class
# This will print "Snowball is 5 years old"
print(yourAverageHuman.Pets[0])

# Print the second element in the Pets list attribute of the yourAverageHuman instance
# The typicalCat instance is the second element in the Pets list attribute of the yourAverageHuman instance
# This will print the returned string from the __str__ function of the typicalCat instance
# This will print "Fluffy likes to sit in the sun ray"
print(yourAverageHuman.Pets[1])

# Print the name attribute of the second element in the Pets list attribute of the yourAverageHuman instance
# The typicalCat instance is the second element in the Pets list attribute of the yourAverageHuman instance
# This will print "Fluffy"
print(yourAverageHuman.Pets[1].name)

# Print the name attribute of the first element in the Pets list attribute of the yourAverageHuman instance
# The huskyDog instance is the first element in the Pets list attribute of the yourAverageHuman instance
# This will print "Snowball"
print(yourAverageHuman.Pets[0].name)
