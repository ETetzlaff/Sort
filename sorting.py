#!/usr/bin/python
import random
import time


#declare first list to sort
list1 = []
for i in range(0,50):
    list1.append(random.randint(0,1000000))

#declare second list to sort
list2 = [] 
for i in range(0,50):
    list2.append(random.randint(0,1000000))


 
def bubbleSort(list):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swap = True


def quickSort(list):
    if len(list) <= 1:
        return list
    end = len(list) - 1
    pivotvar = list[end]

    lowend = []
    highend = []

    for i in list[:end]:
        if i <= pivotvar:
            lowend.append(i)
        else:
            highend.append(i)
            
    sortedList = quickSort(lowend)
    sortedList.append(pivotvar)
    sortedList.extend(quickSort(highend))
    return sortedList
        
        
def mySort(list):
    max = len(list) - 1
    ocounter = 0
    wcounter = 0
    tcounter = 0
    
    while ocounter <= max:
        while wcounter <= max:
            if list[tcounter] > list[wcounter]:
                list[tcounter], list[wcounter] = list[wcounter], list[tcounter]
                tcounter = wcounter
            wcounter += 1
        ocounter += 1
        tcounter = 0
        wcounter = 0
        

#time each sort functionn and compare
t1 = time.time()
sortme = quickSort(list1)
t2 = time.time()
print (t2-t1)*1000.00
print sortme
        
t1 = time.time()
mySort(list1)
t2 = time.time()
print (t2-t1)*1000.00
print list1


t1 = time.time()
bubbleSort(list2)
t2 = time.time()
print (t2-t1)*1000.00
print list2


