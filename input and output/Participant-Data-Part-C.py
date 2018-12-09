##
# Participant Data, Part C Lecture
##

# _*_ coding: utf-8 _*_


# Create the number of participants that are allowed to register
ParticipantNumber = 5
ParticipantData = []  # For now an empty list to store Participant Data

# Create a counter for the registered participants
registeredParticipants = 0

# This is the file where we are going to write our data
outputFile = open("PaticipantData.txt","w")

# Loop over the participants
while(registeredParticipants < ParticipantNumber):
    # Add a temporary data holder as a list
    tempPartData = [] # name, country of origin, age
    # Ask for user input to add his name
    name = input("Please enter your name: ")
    # Append the name to the temporary data
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    # Append the country to the temporary data
    tempPartData.append(country)
    # Ask for user input to add his age
    age = int(input("Please enter your age: "))  # Convert the input to integer
    # Append the age to the temporary data
    tempPartData.append(age)
    # Print the tempData
    print (tempPartData)
    # Save our temporary data to the ParticipantData
    ParticipantData.append(tempPartData)  # [tempPartData] = [[name,country,age]]
    print(ParticipantData)
    # Increase the registeredParticipants number
    registeredParticipants +=1 # = registeredParticipants + 1

# Write everything to a file
# Each participant is represented by a list
for participant in ParticipantData:
    # loop over particpant data
    for data in participant:
        outputFile.write(str(data))  # Convert data to string and write it to the file
        # We need to add extra formatting otherwise we will have it similar to MaxU.s.21
        outputFile.write(" ")  # MaxU.s.21
    # Add each participant data in a new line
    outputFile.write("\n")

# Always remember to close your file
outputFile.close()

# Reading all this data from the file
inputFile = open("PaticipantData.txt","r")
# Store all the file data into an inputList
inputList = []
# Read through the file line by line using a for loop
for line in inputFile:
    # We need to read back from the file all participant data
    tempParticipant = line.strip("\n").split()
    # This is equivalent to the following
    # "Max U.S. 21 \n".strip("\n") -> "Max U.S. 21 "  // Takes out the \n
    # "Max U.S. 21 ".split() -> ["Max","U.S.","21"]  // Split the string and puts it's part into a list
    print(tempParticipant)
    # Let's append the data to the inputList
    inputList.append(tempParticipant)
    print(inputList)

# let's save the data into a dictionnary
Age = {}
# loop over the list to get each participant's age
for part in inputList:
    # Use a temporary variable
    tempAge = int(part[-1])  # ie: int('21') -> 21
    # We can access the last element using this method
    # Only add the Age to the dictionnary if it doesn't exist already
    if tempAge in Age:
        Age[tempAge] += 1 # means there is one more person with the same age
    else:
        Age[tempAge] = 1 # Otherwise, put it inside the dictionnary and give it value 1

print(Age)  # ie: {25: 2, 22: 1, 21: 1, 26: 1}


# We can also get other participant's data like country int(part[1]) or name int(part[0])
Countries = {}
# loop over the list to get each participant's country
for part in inputList:
    # Use a temporary variable
    tempCountry = part[1] # No need to convert : it's already a string
    # We can access the last element using this method
    # Only add the Age to the dictionnary if it doesn't exist already
    if tempCountry in Countries:
        Countries[tempCountry] += 1 # means there is one more person with the same age
    else:
        Countries[tempCountry] = 1 # Otherwise, put it inside the dictionnary and give it value 1

print("Countries that attended:",Countries)

# Find the oldest age
Oldest = 0              # Let's assume this is the minimum value our age can have
Youngest = 100          # Let's assume this is the maximum value our age can have
mostOccuringAge = 0     # To save the most occurant age
counter = 0

# Loop over the Age dictionnary
for tempAge in Age:
    # In the first time Oldest = first tempAge since the previous value was 0
    # In each loop: if we have found a new bigger value, we will assign it to variable Oldest
    if tempAge > Oldest:
        Oldest = tempAge
    # Otherwise, Oldest will not change and we'll assign it to the Youngest
    if tempAge < Youngest:
        Youngest = tempAge
    # Access the value of each key in dictionary, counter will get the value for most occuring age
    if Age[tempAge] >= counter:
       counter = Age[tempAge]
       # Get the dictionnary key equivalent to mostOccurongAge
       mostOccuringAge = tempAge

# Print the Oldest Age
print(Oldest)
print(Youngest)
print("Most occuring age is:",mostOccuringAge,"with",counter,"participants")

# Always remember to close your file
inputFile.close()
