# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:58:13 2019

@author: seanm
"""

def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""
    y, limit, res = 0, min(strs, key=len), ""
    while y < len(limit):
        unique = set()
        for word in strs:
            print(word,res)
            if word[y] not in unique:
                unique.add(word[y])
            if len(unique) > 1:
                return res
        res += unique.pop()
        y += 1
    return res

longestCommonPrefix(['hello','hell','he'])