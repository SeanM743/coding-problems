
def max_water(heights):

    left, right, capacity = 0, len(heights)-1, 0
    
    while left < right:
        capacity = max(capacity, (right - left)* min(heights[left], heights[right]))
        if heights[right] < heights[left]:
            right -= 1
        else: left -= 1
