

def max_subarray(a):

    def max_crossing(l, m, r):
        lmax = rmax = lsum, rsum = 0

        for i in range(m, l-1, -1):
            lsum += a[i]
            if lsum > lmax:
                lmax = lsum

        for i in range(m, r, 1):
            rsum += a[i]
            if rsum > rmax:
                rmax = rsum
        
        return lsum + rsum
        
    def max_helper(l, r):
        if l == r:
            return a[l]
        mid = (l + r) // 2
        return max(max_helper(l, m), max_helper(m + 1, r), 
                max_crossing(l, r)) 

