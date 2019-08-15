# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:41:44 2019

@author: snama
"""

#recursive stairs Amazon interview question

#write this as number of ways to get to top of a staircase assuming you can take x steps


def numSteps(stairs,stepCount):
    
    if stairs <= 1:
        return 1
    
    total = 0
    
    for j in stepCount:
        if j <= stairs:
            total += numSteps(stairs-j,stepCount)
            
    return total

print(numSteps(3,[1,2]))