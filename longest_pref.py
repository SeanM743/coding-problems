# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:30:31 2019

@author: seanm
"""

def longest_pref(strs):
    
    if not strs:
        return ''
    
    y, lim = 0, min(strs,key = len)
    pref = ''
    
    while y < len(lim):
        unique = set()
        
        for word in strs:            
            if word[y] not in unique:
                unique.add(word[y])                
            if len(unique) > 1:
                return pref
            
        pref += unique.pop()
        y += 1
        
    return pref
            
                