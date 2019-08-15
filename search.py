import math

'''find the square root of a non-integer number'''

def square_root(n):

    left,right = ((0,1) if n < 1.0 else (0,n))
    
    while not math.isclose(left,right):
        middle = .5*(left+right)
        sq = middle**2
        if math.isclose(sq,n):
            return middle
        elif sq < n:
            left = middle
        elif sq > n:
            right = middle
    return None

print(square_root(5))

'''Write a function that searches a 2D array of values that are sorted in
ascending order in both row and column

Example:

-1 2 5  7
 2 3 7  9
 5 8 12 19

 '''

def search_grid(grid,search_val):
    #start in top right corner and progressively eliminate rows/column
    row, column = 0, len(grid[0])
    while column > 0 and row < len(grid):
        value = grid[row][column]

        if value == search_val:
                return True
        elif value > search_val:
            row += 1
        else:
            column -= 1

'''write a function that computes the min and max of something in something other than 2*n comparisons'''
import collections

def find_min_max(a):
    MinMax = collections.namedtuple('MinMax',('smallest','largest'))

    def min_max(a,b):
        return MinMax(a,b) if a < b else MinMax(b,a)
    
    global_min_max = min_max(a[0],a[1])
    for i in range(2,len(a)-1):
        local_min_max = min_max(a[1],a[i+1])
        global_min_max.smallest = min(local_min_max.smallest, global_min_max.smallest)
        global_min_max.largest = max(local_min_max.largest, global_min_max.largest)

    if len(a) % 2 == 1:
        global_min_max.smallest = min(a[-1], global_min_max.smallest)
        global_min_max.largest = max(a[-1], global_min_max.largest)
    
    return global_min_max

'''return the kth largest number without sorting or using min-heap'''
def kth_largest(a, k):
    #partition around random pivot, if pivot index is == k, return value in that pivot; otherwise, eliminate some part of array
    left, right = 0, len(a)-1

    def partition_around_pivot(left,right,pivot):
        pivot_value = a[pivot]
        a[right], a[pivot] = a[pivot], a[right]

        new_pivot_index = left
        for i in range(left,right):
            if a[i] < pivot_value:
                a[new_pivot_index], a[i] = a[i], a[new_pivot_index]
                new_pivot_index += 1
            
        a[new_pivot_index], a[right] = a[right], a[new_pivot_index]
        return new_pivot_index

    while left <= right:
        rand_pivot = random.randint(left,right)
        new_pivot_index = partition_around_pivot(left,right,rand_pivot)

        if new_pivot_index == k-1:
            return a[new_pivot_index]
        elif new_pivot_index < k-1:
            left = new_pivot_index + 1
        else:
            right = new_pivot_index -1
    

    




