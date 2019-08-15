# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:47:43 2019

@author: seanm
"""

def intPal(n):
    rev = 0
    while n > rev:
        x = n%10
        n = n//10
        temp = rev*10 + x
        rev = temp
    return rev == n or n == rev//10