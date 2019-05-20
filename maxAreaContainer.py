# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:55:40 2019

@author: seanm
"""

#max area of 2 lines problem: points of line are passed into function via height list. Find the 2 lines with most area

def maxArea(height):
    
    maxa = 0
    l = len(height)
    for i in range(l-1):
        for j in range(l-i):
            base = i+j 
            hgt = min(height[i],height[i+j])
            area = base*hgt
            print(i,j,base,hgt,area)
            if area > maxa:
                maxa = area

                
    return maxa

a = maxArea([1,3,2,7,9])