# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:21:30 2019

@author: seanm
"""

def is_one_away(s1,s2):
    
    if abs(len(s1) - len(s2)) >1:
        return False
    
    p1 = p2 = count = 0;
    
    if len(s1) == len(s2):
        while p1 < len(s1):
            if s1[p1] != s2[p2]:
                count += 1
            p1+=1;p2+=1
        return count <=1
    
    else:
        longer = s1 if len(s1) > len(s2) else s2
        shorter = s1 if len(s1) < len(s2) else s2
        
        while p1 < len(longer)-1:
            if longer[p1] != shorter[p2]:
                count +=1
                p1+=1
            else:
                p1+=1;p2+=1
                
        return count <=1
    
# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False    