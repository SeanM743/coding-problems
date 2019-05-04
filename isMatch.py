# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:08:28 2019

@author: seanm
"""

def isMatch(s: str, p: str) -> bool:
    
    if not p:
        return not bool(s)
    if not s:
        return not bool(p)
    
    match = p[0] in (s[0],'.')
    
    if len(p)>1 and p[1] == '*':        
        return (match and isMatch(s[1:],p)) or (match and isMatch(s[1:],p[2:]))
    else:
        return match and isMatch(s[1:],p[1:])

print(isMatch("aa","a*"))