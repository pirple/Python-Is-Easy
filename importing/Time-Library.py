##
# The Time Library Lecture
##

# _*_ coding: utf-8 _*_

# import the 'time' library and print the time, processor takes to print the "Hello World"
import time

currentTime = time.clock()
print("Hello")
print("World")
pastTime = time.clock()
print(pastTime - currentTime)

# sleep the processor for 3 seconds using 'sleep' function
print("1")
time.sleep(3)
print("2")

# print the integers from 1 to 10 in the interval break of 1 second
for i in range(1,11):
    print(i)
    time.sleep(1)
