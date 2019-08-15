# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:19 2019

@author: seanm
"""

def recMatch(s,cs):
    
    if(s==''):
        return True
    return s[0] == cs[0] and recMatch(s[1:],cs[1:])