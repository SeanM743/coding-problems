def gray_code_generator(num_bits):

    def gray_helper(num_bits):
        if num_bits == 0:
            return ['0']
        if num_bits == 1:
            return ['0', '1']

        partial_solution = gray_helper(num_bits - 1)
        result = ['0' + b for b in partial_solution] 
        result += ['1' + b for b in reversed(partial_solution)]
        return result
    
    
    return gray_helper(num_bits)

#print(gray_code_generator(2))

def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n == 0:
        return [0]
    else:
        pre = grayCode(n-1)
        post = [x + 2**(n-1) for x in pre[::-1]]
        return pre + post

#print(grayCode(3))

def grayCode_verbose(num_bits):

    def grayCode_helper():
        
        def check_bitdiff_one(x,y):
            xor_val = x ^ y
            bit_diff = xor_val & (xor_val -1)
            return xor_val and not bit_diff
        
        if len(result) == 1 << num_bits:
            return check_bitdiff_one(result[0], result[-1])
        
        for i in range(num_bits):
            next_candidate = result[-1]
            shifted_candidate = next_candidate ^ (1 << i)
            if shifted_candidate not in result:
                result.append(shifted_candidate)
                if grayCode_helper():
                    return True
                del result[-1]
        return False

    result = [0]
    grayCode_helper()
    return result

print(grayCode_verbose(3))