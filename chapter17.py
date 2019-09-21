
def max_water(heights):

    left, right, capacity = 0, len(heights)-1, 0
    
    while left < right:
        capacity = max(capacity, (right - left)* min(heights[left], heights[right]))
        if heights[right] < heights[left]:
            right -= 1
        else: left -= 1

def calculate_largest_rectangle(heights):
    max_area, pillars = 0, []

    for i, height in enumerate(heights):
        while height < pillars[-1] and pillars:
            pillar_height = heights[pillars.pop()]
            width = i if not pillars else i - pillars[-1] - 1
            max_area = max(max_area, pillar_height * width)
        
        pillars.append(i)


