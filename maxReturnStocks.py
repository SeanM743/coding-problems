# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:28:03 2019

@author: snama
"""

def maxReturn(prices,mp):
    i = len(prices)
    
    if i <= 1:
        return (prices[0],prices[0],0)

    lmin, lmax, lmp  =  maxReturn(prices[:int(i/2)],mp)
    rmin, rmax, rmp =   maxReturn(prices[int(i/2):],mp)
    
    l = min(lmin,rmin)
    r = max(lmax,rmax)

    mp = max(lmp,rmp, rmax-lmin)
    
    return (l,r,mp)

p = [1, 4, 67, 5, 22]

p2 = [124, 1, 44, 3, 99, 105, 1]
print(maxReturn(p2,0))