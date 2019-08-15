# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:33:36 2019

@author: seanm
"""

#def rotate_array(a):
#    
#    size = len(a)
#    temp = [[0 for i in range(size)] for j in range(size)]
#    for i in range(size):
#        for j in range(size):
#            temp[j][size-i-1] = a[i][j]
#    return temp

#print(rotate_array([[1,2,3],[4,5,6],[7,8,9]]))

def rot_inplace(a):
    
    size = len(a)
    i,j,new_i,new_j,temp,count = 0,0,0,a[0][0],0
    
    while count<size-1:
        new_i = size-1-j
        new_j = i
        target = a[new_i][new_j]
        a[new_i][new_j] = temp
        temp = target
        i = new_i
        j = new_j
        count+=1
        
    return a

print(rot_inplace([[1,2,3],[4,5,6],[7,8,9]]))