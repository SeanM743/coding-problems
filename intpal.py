# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:56:12 2019

@author: seanm
"""

#This version reverses the integer and compares it to the original int. If they are equal it's a palindrome

def intPal(n):
    rev = 0
    revn = n
    while revn >= 1:
        x = revn%10
        revn = revn//10
        temp = rev*10 + x
        rev = temp
    return rev == n

        