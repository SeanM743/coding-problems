# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:02:51 2019

@author: seanm
"""

def maxArea(height):
    l = len(height) -1
    beg, end = 0, l
    maxarea = 0
    
    while(beg != end):
        h = min(height[beg],height[end])
        base = end-beg
        area = base*h
        
        if area>maxarea:
            maxarea = area
        
        if height[beg+1] > height[end-1]:
            beg = beg+1
        else:
            end = end-1
    return maxarea



print(maxArea([1,8,6,2,5,4,8,3,7]))