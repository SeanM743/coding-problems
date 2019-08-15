# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:33:07 2019

@author: seanm
"""
def isMatch(s,p):
    memo={}
    
    def dp(i,j):
        if (i,j) not in memo:
            
            if j == len(p):
                return i == len(s)
            
            match = i < len(s) and p[j] in {s[i],'.'}
            
            if j+1 < len(p) and p[j+1] == '*':
                ans = match and dp(i+1,j) or dp(i,j+2)
            else:
                ans = match and dp(i+1,j+1)
            
            memo[i,j] = ans
        
        return memo[i,j]
        
    
    return dp(0,0)


print(isMatch('helllllllllo','hell*o'))
