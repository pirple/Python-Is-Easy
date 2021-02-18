# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:51:10 2021

@author: Walter Anderson
"""

Assignment = "HomeWork 4 - lists"

# Create a global variable called "myUniqueList" and be empty to start
# Create a function to add things and check things that are trying to be added
# only add unique items when one is identified return True
# on duplicates don't add but keep track of them by identifying them as False
# 
# for this excercize my assumption is that we will be rolling a die to obtain
# randum numbers for this excersize. (I formally had tried this to obtain
# all 6 sides of a single die, it took 25 rolls, which exceeded my learning 
# so far, so I am redoing the excercize with a limited number of randum
# numbers to complete this exercize and learn more)

# I am going to collect 10 randum numbers to try again using 
#  randum.org/dice/ to roll the die..

myRollList = [10,5,3,1,6,4,4,5,4,5]
#Index[0], identifies the total number of items in the list

MyRollListIndex = myRollList[0]

FirstPass = True

Pass = True

End = False

Cycles = 1

Item = 0

HoldRollItem = 0

NewUniqueItem = True

Chk01 = 0
Chk02 = 0
Chk03 = 0
Chk04 = 0
Chk05 = 0
Chk06 = 0
Chk07 = 0
Chk08 = 0
Chk09 = 0
Chk10 = 0
Chk11 = 0


#create two empty lists

myUniqueList = []

myLeftOverList = []

#this sets up position 0 to be an index tracker

myUniqueList.append(0)

MyUniqueIndex = 1

myUniqueList[0] = MyUniqueIndex


myLeftOverList.append(0)
MyLeftOverIndex = 1

myLeftOverList[0] = MyLeftOverIndex


#Start Sub-routines

def readRoll(Num,):
    
    MyRollReadIndex = int(Num)
    HoldRollItem = myRollList[MyRollReadIndex]
    
       
    return HoldRollItem

def readUnique(CheckIndex):
    CheckUniqueItem = readUnique(CheckIndex)
    
    return CheckUniqueItem

def writeUnique(HoldRollItem, MyUniqueIndex):
    myUniqueList.append(HoldRollItem)
    MyUniqueIndex = MyUniqueIndex + 1
    myUniqueList[0] = MyUniqueIndex
    
    return MyUniqueIndex

def writeLeftOvers(HoldRollItem,MyLeftOverIndex):
    myLeftOverList.append(HoldRollItem)
    MyLeftOverIndex = MyLeftOverIndex + 1
    myLeftOverList[0] = MyLeftOverIndex
    
    return MyLeftOverIndex

#End Sub-routines

#Start Main Loop


if Pass == True and Cycles <= MyRollListIndex:
    
    if FirstPass == True:
        MyRollReadIndex = 1
        
        HoldRollItem = readRoll(MyRollReadIndex)
        
        Chk01 = HoldRollItem
        PassNum = 1
        myUniqueList.append(HoldRollItem)
        MyUniqueIndex = MyUniqueIndex + 1
        myUniqueList[0] = MyUniqueIndex
       
        FirstPass = False
        Cycles = Cycles + 1
        
    
    
    while Pass == True and Cycles <= 10:
        
       
        
        MyRollReadIndex = Cycles
        HoldRollItem = myRollList[MyRollReadIndex]
        
        if Cycles == 2:
            Chk02 = HoldRollItem
           
           
        if Cycles == 3:
            Chk03 = HoldRollItem
                
        if Cycles == 4:
            Chk04 = HoldRollItem
            
        if Cycles == 5:
            Chk05 = HoldRollItem
            
        if Cycles == 6:
            Chk06 = HoldRollItem
            
        if Cycles == 7:
            Chk07 = HoldRollItem
             
        if Cycles == 8:
            Chk08 = HoldRollItem    
             
        if Cycles == 9:
            Chk09 = HoldRollItem 
            
        UniqueItemstoCheck = MyUniqueIndex-1
        
        if UniqueItemstoCheck == 1:
            if Chk01 != Chk02:
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 2:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk02 != Chk03):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 3:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk01 != Chk04
                and Chk02 != Chk03
                and Chk02 != Chk04
                and Chk03 != Chk04):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 4:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk01 != Chk04
                and Chk01 != Chk05
                and Chk02 != Chk03
                and Chk02 != Chk04
                and Chk02 != Chk05
                and Chk03 != Chk04
                and Chk03 != Chk05
                and Chk04 != Chk05):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 5:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk01 != Chk04
                and Chk01 != Chk05
                and Chk01 != Chk06
                and Chk02 != Chk03
                and Chk02 != Chk04
                and Chk02 != Chk05
                and Chk02 != Chk06
                and Chk03 != Chk04
                and Chk03 != Chk05
                and Chk03 != Chk06
                and Chk04 != Chk05
                and Chk04 != Chk06
                and Chk05 != Chk06):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 6:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk01 != Chk04
                and Chk01 != Chk05
                and Chk01 != Chk06
                and Chk01 != Chk07
                and Chk02 != Chk03
                and Chk02 != Chk04
                and Chk02 != Chk05
                and Chk02 != Chk06
                and Chk02 != Chk07
                and Chk03 != Chk04
                and Chk03 != Chk05
                and Chk03 != Chk06
                and Chk03 != Chk07
                and Chk04 != Chk05
                and Chk04 != Chk06
                and Chk04 != Chk06
                and Chk05 != Chk06
                and Chk05 != Chk07
                and Chk06 != Chk07):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 7:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk01 != Chk04
                and Chk01 != Chk05
                and Chk01 != Chk06
                and Chk01 != Chk07
                and Chko1 != Chk08
                and Chk02 != Chk03
                and Chk02 != Chk04
                and Chk02 != Chk05
                and Chk02 != Chk06
                and Chk02 != Chk07
                and Chk02 != Chk08
                and Chk03 != Chk04
                and Chk03 != Chk05
                and Chk03 != Chk06
                and Chk03 != Chk07
                and Chk03 != Chk08
                and Chk04 != Chk05
                and Chk04 != Chk06
                and Chk04 != Chk06
                and Chk05 != Chk06
                and Chk05 != Chk07
                and Chk05 != Chk08
                and Chk06 != Chk07
                and Chk06 != Chk08
                and Chk07 != Chk08):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
                
        if UniqueItemstoCheck == 8:
            if (Chk01 != Chk02
                and Chk01 != Chk03
                and Chk01 != Chk04
                and Chk01 != Chk05
                and Chk01 != Chk06
                and Chk01 != Chk07
                and Chk01 != Chk08
                and Chk01 != Chk09
                and Chk02 != Chk03
                and Chk02 != Chk04
                and Chk02 != Chk05
                and Chk02 != Chk06
                and Chk02 != Chk07
                and Chk02 != Chk08
                and Chk09 != Chk09
                and Chk03 != Chk04
                and Chk03 != Chk05
                and Chk03 != Chk06
                and Chk03 != Chk07
                and Chk03 != Chk08
                and Chk03 != Chk09
                and Chk04 != Chk05
                and Chk04 != Chk06
                and Chk04 != Chk06
                and Chk05 != Chk06
                and Chk05 != Chk07
                and Chk05 != Chk08
                and Chk05 != Chk09
                and Chk06 != Chk07
                and Chk06 != Chk08
                and Chk06 != Chk09
                and Chk07 != Chk08
                and Chk07 != Chk09
                and Chk08 != Chk09):
                NewUniqueItem = True
            else:
                NewUniqueItem = False
        
        if NewUniqueItem == True:
            AddUniqueItem = HoldRollItem
            Add = writeUnique(AddUniqueItem, MyUniqueIndex)
            
            MyUniqueIndex = MyUniqueIndex + 1
            
        else:
            # if not write to LeftOvers
            AddLeftOverItem = HoldRollItem
            Add = writeLeftOvers(HoldRollItem, MyLeftOverIndex)
            
            MyLeftOverIndex = MyLeftOverIndex + 1
       
        
        Cycles = Cycles + 1
        
        if Cycles <= 9:
            
          print("getting close")
        
        else:
            
            Pass = False
            
    print("my UniqueList =", myUniqueList)
    print(" myLeftOverList =", myLeftOverList)
        
