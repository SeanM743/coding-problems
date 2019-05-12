# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:16:54 2019

@author: snama
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 12 09:44:24 2019

@author: snama
"""

def subsetSum(checkSet, total, i, mem):
    
    keyval = str(i) + ':' + str(total)
    
    if keyval in mem:
        return mem[keyval]
    
    if total == 0:
        return 1
    
    elif i < 0 or total <0:
        return 0
    
    elif checkSet[i] > total:
        temp = subsetSum(checkSet,total,i-1,mem)
    
    else:
        temp = subsetSum(checkSet,total-checkSet[i],i-1,mem) + subsetSum(checkSet,total,i-1,mem)
    
    mem[keyval] = temp
    return mem[keyval]

mem = {}
s = [2,4,6,10,22,65,43,19,13,3,4,4,4,4]
print(subsetSum(s,16,len(s)-1,mem))
