# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:46:08 2019

@author: snama
"""

def enums(m):
    val = []
    
    if len(m) == 0:
        return []
    if len(m) == 1:
        return m
    
    for i in range(0,len(m)):
        z = m[i]
        
        #val.append(m[i])
        rem = m[:i] + m[i+1:]
        
        for p in enums(rem):
            val.append(z + p)
    
    return val