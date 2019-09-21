def hanoi_towers(num_disks, from_tower, to_tower, using_tower):
    
    def tower_helper(num_disks, from_tower, to_tower, using_tower):
        if num_disks > 0:
            towers(num_disks -1, from_tower, using_tower, to_tower)
            print('Move from peg ', from_tower, 'to peg ', to_tower)
            towers[to_tower].append(towers[from_tower].pop())
            towers(num_disks -1, using_tower, to_tower, from_tower)
    
    NUM_PEGS = 3
    towers = [list(reversed(range(1, num_disks + 1)))]  + [[] for _ in range(1, NUM_PEGS)]
        
def hanoi_towers2(num_disks, from_tower, to_tower, using_tower):

    if num_disks == 1:
        print('Move from', from_tower, 'to tower ', to_tower)
    else:
        hanoi_towers2(num_disks-1, from_tower, using_tower, to_tower)
        hanoi_towers2(1, from_tower, to_tower, using_tower)
        hanoi_towers2(num_disks -1, using_tower, to_tower, from_tower)

def non_attacking_queens(n = 4):

    def check_queen(row):
        if row == n:
            result.append(col_placement) 
            return
        for col in range(n):
            if all(abs(col - c) not in (0, row-i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                check_queen(row + 1)
    col_placement = [0] * n
    result = []
    check_queen(0)

def power_set(input_set):

    def power_helper(to_be_selected, selected_so_far):
        
        if to_be_selected == len(input_set):
            results.append(selected_so_far)
            return
        
        power_helper(to_be_selected + 1, selected_so_far)
        power_helper(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])
    
    results = []
    power_helper(0, [])
    return results

# input_set = [0,1,3,9]
# print(power_set(input_set))

#generate all size k subsets of set of length n {1,2,3...n}

def k_subsets(k, n):

    def k_helper(i, partial_subset):
        if k == len(partial_subset):
            results.append(partial_subset)
        
        remaining = k - len(partial_subset)
        
        while i < n and remaining < n - i + 1:
            k_helper(i+1, partial_subset + [i])
            i += 1
        
    results = []
    k_helper(0, [])
    return results


#recursively build program that generates all possible matching paren strings of length k

def gen_paren(k):

    def paren_helper(left_remain, right_remain, valid_pref, results = []):
        if left_remain > 0:
            paren_helper(left_remain - 1, right_remain, valid_pref + '(')
        if left_remain < right_remain: 
            paren_helper(left_remain, right_remain -1, valid_pref + ')')
        if not right_remain:
            results.append(valid_pref)
        return results

    return paren_helper(k, k, '')


#print(gen_paren(4))

def pal_partitioning(s):

    def pal_helper(offset, partial_pal):
        if offset == len(s):
            results.append(list(partial_pal))
            return

        for i in range(offset + 1, len(s) + 1):
            pref = s[offset:i]
            if pref == pref[::-1]:
                pal_helper(i, partial_pal + [pref])

    results = []
    pal_helper(0, [])
    return results

#print(pal_partitioning('aabbccdf'))

def gen_bin_tree(num_nodes):
    if num_nodes == 0:
        return [None]
    result = []

    for num_left_nodes in range(num_nodes):
        num_right_nodes = num_nodes - num_left_nodes - 1
        left_tree = gen_bin_tree(num_left_nodes)
        right_tree = gen_bin_tree(num_right_nodes)
        result += [BinaryTree(0, left_tree, right_tree) for left in left_tree for right in right_tree]
    
    return result

def check_suduko(partial_solution):
    EMPTY_VAL = 0

    def find_soln(i, j):
        if i == len(partial_solution):
            i = 0
            j += 1
            if j == len(partial_solution):
                return True

        if partial_solution[i][j] != EMPTY_VAL:
            find_soln(i+1, j)

        def check_if_valid(i, j, val):
            #check row valid
            if any(val == partial_solution[k][j] for k in range(len(partial_solution))):
                return False
            
            if val in partial_solution[i]:
                return False
            
            gsize = int(math.sqrt(len(partial_solution)))
            I = i // gsize
            J = j // gsize

            if val in [x for x in partial_solution[gsize*I + a][gsize*J + b] 
            for a,b in itertools.product(range(gsize), repeat = 2)]:
                return False
            
        for val in range(1, len(partial_solution) + 1):
            if valid_soln(i, j, val):
                partial_solution[i][j] = val
                if find_soln(i+1, j, partial_solution):
                    return True

        partial_solution[i][j] == EMPTY_VAL
        return False
    
    return find_soln(0,0)
    
def gray_code_generator(num_bits):

    def calculate_gray(history):

        def one_bit_diff(a, b):
            bitdiff =  a ^ b
            return bitdiff and not (bitdiff & (bitdiff -1))
        
        if len(results) == 1 << num_bits:
            return one_bit_diff(results[0], results[-1])

        for shift in range(num_bits):
            next_candidate = results[-1] 
            shift_mask = 1 << shift
            shifted_candidate = next_candidate ^ shift_mask
            if shifted_candidate not in results:
                history.add(shifted_candidate)
                results.append(shifted_candidate)
                if calculate_gray(history):
                    return True
                history.remove(shifted_candidate)
                del results[-1]
        return False
    
    results = [0]
    calculate_gray(set([0]))
    return results
#print(gray_code_generator(3))

def gray_code_generator2(n):
    if n == 0:
        return [0]    
    gc_minus_one = gray_code_generator2(n-1)
    print(gc_minus_one)

    return gc_minus_one + [(1 << (n-1)) | i for i in reversed(gc_minus_one)]

print(gray_code_generator2(3))

def gray_code_generator3(n):
    result = [0]
    for i in range(n):
        result += [b + 2**i for b in reversed(result)]
    return result
    

