# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:57:05 2019

@author: seanm
"""

def permu(st):
    
    num = len(st)
    print("called perm",st,st[0])
    if num == 1:
        print("returned ", st[0])
        return st[0]
    out = []
    
    for i in range( len(st)):
        print("for loop #",i,out)
        print(st[0],st[1:],num)
        p = st[0] + permu(st[1:])
        out.append(p)
#        st[0],st[i] = st[1],st[0]
#        print(st[0] + permu(st[1:]))
    
    return out
print(permu(list('abc')))