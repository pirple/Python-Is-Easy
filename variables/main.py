##
# Variables Lecture
##

# -*- coding: utf-8 -*-


PI = 3.14
print(PI)

#one = 1
#two = 2
#three = 3

one, two, three = 1, 2, 3

print(one)
print(two)
print(three)
two = 4
print(two)
print(one)

Decimal = 1.1
print(Decimal)

StringVar = "Hello" + "1"
print(StringVar)

def FunctionName():
    global one
    newVar = "World"
    print(one)
    print(newVar)
    return

FunctionName()
# print(newVar)

# Left = what you're giving the value to
# Right = What the value is
Five = 3+2
print(Five)

# 5 = Five
# Five + Six = 3+2

count = 0
print(count)

count = count + 1
print(count)

#count += 1
#print(count)

#count *= 3
#print(count)

count /= 3
print(count)
