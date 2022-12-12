##
# "If" Statements Lecture
##

# -*- coding: utf-8 -*-

'''
Syntax:
if condition:
    Action
'''
click = False                 #set variable click to False
Like = 0                      #initialize Like equal to 0

if click == True:             #Check if click is True
    Like = Like + 1           #Increment Like by 1
    click = False             #set click to False

print(Like)                  #print the value
Temperature = 20             #set a variable Temperature to 20
Thermo = 15                  #set a variable Thermo to 15
if Temperature < 15:         #Check if Temperature is less than 15
    Thermo = Thermo + 5      #if yes increment variable Thermo by 5

print(Thermo)               #print the value Thermo

Temperature = 14             #set variable Temperature to 14
Thermo = 15                  #set variable Thermo to 15
if Temperature < 15:         #Check if Temperature is less than 15
    Thermo = Thermo + 5      #if True increment Thermo by 5

print(Thermo)               #print the value of Thermo

Temperature = 15            #set variable Temperature to 15
Thermo = 15                 #set variable Thermo to 15
if Temperature <= 15:       #Check if Temperature is less than or equal to 15
    Thermo = Thermo + 5     #if True increment Thermo by 5

print(Thermo)               #print the value of Thermo

if Temperature > 20:        #Check if Temperature is greater than 20
    Thermo = Thermo - 3     #if True decrement Thermo by 3

print(Thermo)               #print the value of Thermo
Temperature = 20           #set the value of Temperature to 20
Thermo = 15                #set Thermo equals to 15
if Temperature <= 15:      #Check if Temperature is less than or equal to 15
    Thermo = Thermo + 5    #if True increment Thermo by 5

print(Thermo)              #print value of Thermo

if Temperature >= 20:       #Check if Temperature is greater than or equal to 20
    Thermo = Thermo - 3     #if True decrement Thermo by 3

print(Thermo)              #print value of Thermo


Time = "Day"               #set variable Time to Day
Sleepy = False             #set Sleepy equals to False
Pajamas = "Off"            #initialize Pajamas equal to Off
'''
If Time equals to Night and Sleep is True then set Pajamas equal to On
'''
if Time == "Night" and Sleepy == True:   #Check two condition and are ANDed
    Pajamas = "On"                       #if both condition are True then set Pajamas = On
print(Pajamas)                            #print the value of Pajamas

Pajamas = "Off"             #initialize Pajamas equal to Off
if Time == "Night" or Sleepy == True:    #Check two condition and are ORed
    Pajamas = "On"                       #if anyone of the condition is True set Pajamas equal to On
print(Pajamas)                           #print the value of Pajamas

Time = 'Night'                #set variable Time to Night
Sleepy = 'True'               #set variable Sleep equals to True
Pajamas = "Off"               #initialize Pajamas equal to Off
if Time == "Night" or Sleepy == False: #Check two condition and are ORed
    Pajamas = "On"              #if anyone of the condition is True set Pajamas equal to On
print(Pajamas)                #print the value of Pajamas

'''
intialize Time equals to Day, Sleepy equals to False, Pajamas to off and InBed equals to True
Check if Time equals to Night, set Pajamas equals to On, else if Time equals to Morning is True
set Pajamas equals to On and then print its value
'''
Time = 'Day'
Sleepy = 'False'
Pajamas = "off"
InBed = True
if Time == "Night":
    Pajamas = "On"
elif Time == "Morning":
    Pajamas = "On"
print(Pajamas)

Time = 'Morning'              #set Time equals to Morning
Sleepy = 'False'              #Set Sleepy to False
Pajamas = "Unknown"           #set Pajamas to Unknown
InBed = True                  #set InBed variable to True
print(Pajamas)                #print value of Pajamas
if Time == "Night":           #if Time is equal to Night
    Pajamas = "On"            #set pajamas to On
elif Time == "Morning":       #else if Time equal to Morning
    Pajamas = "On"            #set pajamas to On
else:                          #otherwise if any of the above two statement are not true
    Pajamas = "Off"           #set Pajamas Off
print(Pajamas)                #print the value of Pajamas
