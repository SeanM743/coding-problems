# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:29:49 2019

@author: seanm
"""

class Solution:
    def myAtoi(self, s: str) -> int:

        toci = '1234567890'
        tocs = '+-'
        t = ''

        s = s.strip()

        if s=='':
            return 0
        
        if(s[0] not in toci and s[0] not in tocs):
            return 0

        if s[0] in tocs:
            t+= s[0]
            s = s[1:]

            if s == '' or s[0] not in toci:
                return 0

        for c in s:
            if c in toci:
                t+= c
            else:
                break
    
        t = int(t)
        
        if t > 2**31-1:
            return 2**31-1
        elif t < -2**31:
            return -2**31
        else:
            return t
        
    
    
    