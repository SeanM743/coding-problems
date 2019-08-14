
#print([x for i,x in enumerate(a) if x in b and (i == 0 or x != a[i-1])])

import bisect
def intersect_lists2(a,b):
    
    ordered = (a,b) if len(a) > len(b) else (b,a)

    def is_present(element):
        i = bisect.bisect_left(ordered[0], element)
        return i < len(ordered[0]) and ordered[0][i] == element
    
   
    return [e for i, e in enumerate(ordered[1]) if is_present(e) 
            and (i == 0 or e != ordered[1][i-1])]

a = [1,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]
b = [1,3,7]

print(intersect_lists2(a,b))

    