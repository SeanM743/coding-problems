# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:28:24 2019

@author: seanm
"""

def reverse(x: int) -> int:
    st = str(abs(x))
    
    rev = ''
    for i in st[::-1]:
        rev += i
    rev = int(rev)
    if x <0:
        rev = -1*rev
    if (x > 2**31-1) or (x < -2**31):       
        return 0
    
    return rev

print(reverse(-123))