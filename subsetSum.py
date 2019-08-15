# -*- coding: utf-8 -*-
"""
Created on Sun May 12 09:44:24 2019

@author: snama
"""

def subsetSum(checkSet, total, i):
    
    if total == 0:
        return 1
    
    elif i <0 or total <0:
        return 0
    
    elif checkSet[i] > total:
        return subsetSum(checkSet,total,i-1)
    
    else:
        return subsetSum(checkSet,total-checkSet[i],i-1) + subsetSum(checkSet,total,i-1)
    

print(subsetSum([2,4,6,10,16,8,8],16,6))
