##
# "If" Statements Lecture
##

# -*- coding: utf-8 -*-


# if condition:
#    Action

click = False

Like = 0

click = True

if click == True:
    Like = Like + 1
    click = False

# print(Like)

Temperature = 20
Thermo = 15
# print(Thermo)
if Temperature <=  15:
    Thermo = Thermo + 5

# print(Thermo)

if Temperature >= 20:
    Thermo = Thermo - 3

# print(Thermo)

Time = "Day"
Sleepy = False
Pajamas = "Unknown" 
InBed = True

print(Pajamas)

if Time == "Night" or Sleepy == True:
    Pajamas = "On"

elif Time == "Morning":
    Pajamas = "On"

else:
    Pajamas = "Off"


print(Pajamas)
