##
# File Input and Output Lecture
##

# _*_ coding: utf-8 _*_


# Genral form to open a file with an option ("r":read, "w": write, "a": append, "r+": read and write)
# File = open("Filename","r") # "r", "w", "a", "r+"
# Once done with the file we can close it
# File.close()

# Create a list: sperate elements by a comma
Countries = ["London", "Paris", "New York", "Utah", "IceLand"]
# Let's call our list a VacationSpots
VacationSpots = ["London", "Paris", "New York", "Utah", "IceLand"]

# Creat a file
# The option "w" will create the file if it doesn't exist but will override it if it exists already
# This will create the file at the same folder of your python file code
VacationFile = open("VacationPlaces","w")

# We loop over our list to take each element and put it inside our file
for Spots in VacationSpots:
    VacationFile.write(Spots) # Spots in this case has to be a string
    # Or convert it to string if it is not
    # VacationFile.write(str(Spots))

# close the file
VacationFile.close()
print("done")

# Open the file again: it is not mandatory to use the same variable
VacationFile = open("VacationPlaces","r")

# The following instruction will read all the content of our file and assign it to TheWholeFile
# Note: this is usefull for small files but we will see other methods for bigger files
TheWholeFile = VacationFile.read()
print(TheWholeFile)
# Always close the file once done using it
VacationFile.close()

# We notice that the ouptut doesn't look very well
# The pointer will just write any new element directly after the previous one
# LondonParisNew YorkUtahIceLand

# To solve this: we can add a space after each write operation
VacationFile = open("VacationPlaces","w")
for Spots in VacationSpots:
    # VacationFile.write(Spots+ " ")
    # Or to separate them by ","
    # VacationFile.write(Spots+ ", ")
    # We can also put elements in a new line
    VacationFile.write(Spots+ "\n")
VacationFile.close()

# We can read the file one by one
# Line will have all the data for one line
VacationFile = open("VacationPlaces","r")

# We can read each line into a variable
# We have a pointer that will read the file from the beginning
FirstLine = VacationFile.readline()
print(FirstLine)
# If we read the line again, the pointer will move to the next element
SecondLine = VacationFile.readline()
print(SecondLine)

# In this case we will start by the third line
for line in VacationFile:
    print(line)  # We will a blank line separator since we have put \n between our elements
    # To specify how the end of line should be
    print(line, end = "")  # take away the newLine
VacationFile.close()

# Append a new spot
FinalSpot = "Thailand\n"
# Remember to not use "w" option, otherwise all the content of the file will be deleted
VacationFile = open("VacationPlaces", "a") # use the append option
# Write to the end of the file
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces","r") # Open file as reading
# Loop over the file, line by line
for line in VacationFile:
    print(line, end = "")
VacationFile.close()

# Another method to open a file without having to close it at the end
# The file will be saved inside the variable VacationFile
with open("VacationPlaces","r") as VacationFile:
    for line in VacationFile:
        print(line)
# The file is closed automatically

# So the below instruction is no more valid since file is already closed
# VacationFile.read()

"""
# We can do the above operation for multiple files
# Example : read the content from 5 files (VacationPlaces1 ... VacationPlaces4)
for i in range(5):
    with open("VacationPlaces"+str(i),"r") as VacationFile:
        for line in VacationFile:
            print(line)
"""
