import heapq

'''write a function that returns the kth largest element using heaps'''

def kth_largest(lists, k):
    min_heap,result = [],[]
    iter_lists = [iter(list) for list in lists]

    for idx,list_num in enumerate(iter_lists):
        i,val = idx, next(list_num)
        heapq.heappush(min_heap,(val,i))
    
    while min_heap:
        curr_val, idx = heapq.heappop(min_heap)
        result.append(curr_val)
        smallest_val = next(iter_lists[idx], None)
        if smallest_val is not None:
            heapq.heappush(min_heap, (smallest_val, idx))    
    return result

a = [[1,3,5], [6,9,32],[12,54,99]]
print(kth_largest(a,5))
