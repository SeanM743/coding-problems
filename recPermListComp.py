# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:30:04 2019

@author: seanm
"""

def permRec(ltrs):
    
    p = []
    
    if len(ltrs) == 1:
        return [ltrs]
    for a in ltrs:
        c = [x for x in ltrs if a != x]
        remain_perms = permRec(c)
        
        for t in remain_perms:
            p.append([a] + t)
    return p

print(permRec(['a','b','c']))