# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:42:21 2019

@author: seanm
"""

def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    #populate the bombs
    for x,y in bombs:
        field[x][y] = -1
    
    for row,column in bombs:
        for i in range(row-1,row+2):
            for j in range(column - 1, column+2):
                if i >= 0 and i < num_rows and j>=0 and j < num_cols and field[i][j] != -1:
                    field[i][j] += 1
    return field

def click(field, num_rows, num_cols, given_i, given_j):
    
    if field[given_i][given_j] == -1:
        return field
    to_check = [(given_i,given_j)]
    
    field[given_i][given_j] = -2
    
    while(to_check):
        x,y = to_check.pop(0)
        for i in range(x-1,x+1):
            for j in range(y-1,y+1):
                if i >= 0 and i<= num_rows and j>= 0 and j<= num_cols and field[i][j] != -1:
                    if field[i][j] == 0:
                        to_check.append((x,y))
                        field[i][j] = -2
    return field

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]