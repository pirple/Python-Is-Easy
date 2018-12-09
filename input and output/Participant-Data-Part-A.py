##
# Participant Data, Part A Lecture
##

# _*_ coding: utf-8 _*_


# Create the number of participants that are allowed to register
ParticipantNumber = 2
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


outputFile.close()
