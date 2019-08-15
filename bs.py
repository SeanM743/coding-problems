t = [1,2,899,23,140,10,33,91,44,77,15]

t.sort()

print(t)

def bs(target, left,right, values):
    
    if not values:
        return None
    
    idx = left + (right-left)//2
    
    if left > right:
        return None

    if target == values[idx]:
        return idx
    
    elif target > values[idx]:
        return bs(target, idx+1, right, values)
    
    else:
        return bs(target,left,idx-1, values)
    
    return None

print(bs(899,0,len(t)-1,t))