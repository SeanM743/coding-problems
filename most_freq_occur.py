# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:49:17 2019

@author: seanm
"""

# Implement your function below.
def most_frequent(given_list):
  
    if not given_list return None
    d = {}
    for i in given_list:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    return max(d,key=d.get)

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]