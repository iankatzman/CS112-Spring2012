#!/usr/bin/env python

import math

def ptop((x1, y1), (x2, y2)):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = int(raw_input("enter a number for x1: "))
y1 = int(raw_input("enter a number for y1: "))
x2 = int(raw_input("enter a number for x2: "))
y2 = int(raw_input("enter a number for y2: "))
print "the distance between those points is: ",ptop((x1, y1), (x2, y2))



