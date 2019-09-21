def football_scoring(points, ways_to_score):

    scoring_solutions = [[1] + [0] * points for _ in ways_to_score]

    for i in range(len(ways_to_score)):
        for j in range(1, points + 1):
            prev_solution = (scoring_solutions[i-1][j] if i >= 1 else 0)
            new_solution = (scoring_solutions[i][j - ways_to_score[i]] 
                  if j >= ways_to_score[i] else 0)
            scoring_solutions[i][j] = (prev_solution + new_solution)

    return scoring_solutions

print(football_scoring(10, [2,3,7]))

def max_sum_subarray(A):
    for running_sum in itertools.accumulate(A):
        min_sum = min(running_sum, min_sum)
        max_sum = max(running_sum, max_sum - min_sum)
    return max_sum

def l_distance(A, B):
    
    def l_helper(A_idx, B_idx):

        if A_idx < 0:
            return B_idx + 1
        if B_idx < 0:
            return A_idx + 1
        if distance[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance[A_idx][B_idx] = l_helper(A_idx -1, B_idx -1)        
            else:
                min_distance = 1 + min(l_helper(A_idx -1, B_idx), l_helper(A_idx, B_idx-1),
                        l_helper(A_idx-1, B_idx-1))
                distance[A_idx][B_idx] = min_distance
        return distance[A_idx][B_idx]

    distance = [[-1] * len(B) for _ in len(A)]
    return l_helper(len(A) - 1, len(B) - 1)

def pretty_printing(words, line_len):

    num_spaces = line_len - len(words[0])
    messiness = [num_spaces**2] + [math.inf for _ in range(len(words) - 1)]

    for i in range(1, words):
        num_spaces = line_len - len(words[i])
        messiness[i] = messiness[i-1] + num_spaces**2

        for j in reversed(range(i)):
            num_spaces -= words[j] + 1
            if num_spaces < 0:
                break
            first_j_messiness = 0 if j-1 < 0 else messiness[j-1]
            messiness[i] = min(messiness[i], num_spaces**2 + first_j_messiness)
    return messiness[-1]
    
    def coin(coins, amount):

        def coin_change(val, coin_num):

            if val < 0:
                return float('inf')
            
            if val == 0:
                cache[val] = 0
                return cache[val]
            
            min_val = min(coin_change(val, coin_num + 1), 1 + coin_change(val - coins[coin_num], coin_num))
            cache[val] = min_val
            return min_val
    
        cache = {}
        dp = [float('inf') for _ in coins]
        return coin_change(amount, 0)
    
    def coin2(coins, amount):
        dp = [-1 for _ in coins]

        def coin_helper(amount):

            if amount < 0:
                return -1
            
            if amount == 0:
                return 1

            lowest = float('inf')
            for coin in coins:
                res = coin_helper(amount - coin)
                if res >= 0 and res < lowest:
                    lowest = 1 + res
            dp[amount] = float('inf') if lowest == float('inf') else lowest
            return dp[amount]

                


