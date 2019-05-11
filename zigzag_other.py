# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:09:47 2019

@author: snama
"""

def convert(s: str, numRows: int) -> str:
	if numRows==1:
		return s
	res = ['']*numRows
	interval = 2*(numRows-1)
		
    for i in range(len(s)):
		rem = i%interval
			
        if rem <= numRows-1:
			res[rem]+=s[i]
		else:
			res[interval-rem]+=s[i]
    print(interval,rem)

	return ''.join(res)
    
print(convert('PAYPALISHIRING',3))