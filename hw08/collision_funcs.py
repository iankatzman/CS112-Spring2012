#!/usr/bin/python env

def point_in_box(pt, box):
    x1,y1 = pt
    x2,y2,w,h = box
    return y1 >= y2 and y1 < y2 + h and x1 >= x2 and x1 < x2 + w




