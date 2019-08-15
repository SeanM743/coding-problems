# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:57:12 2019

@author: snama
"""

def zigZag(s,n):
    
    down = True

    if len(s) <= 1:
        return s
    
    
    st = [[] for i in range(n)]
    st[0].append(s[0])
    s = s[1:]
    charleft = len(s) - 1
    
    row = 1
    while charleft >= 0:
        st[row].append(s[0])
        s = s[1:]
        if row == 0 or row == n-1:
            down = not(down)
    
        step = 1 if down else -1
        row = row + step

        charleft -= 1
        r = ''.join([''.join(st[i]) for i in range(n)])
    return r
        
s1 = zigZag('A',2)