def min_path_triangle(triangle):
    length = [0 * len(triangle)]

    for row in triangle:
        length = [row[j] + min(length[max(0,j-1)], length[min(j, len(length - 1))]) 
        
        for j in len(row)]
    
    return min(length)


def min_coin(coin_vals, coin):
    dp = [0] + [coin+1]* coin

    for j in range(1, len(dp)):
        dp[j] = 1 + min(dp[j-i] for i in coin_vals if (j-i) >= 0)
    print(dp)
    return dp[-1]

def top_down_min_coin(coin_vals, coin):

    def top_dp_coin(coin):

        if coin == 0:
            return 0
        min_val = 1000
        for v in coin_vals:
            if coin - v >= 0:                
                result = 1 + top_dp_coin(coin - v)
                if result < min_val:
                    min_val = result
        return min_val

    return top_dp_coin(coin)  



coins = [9, 6, 5, 1] 
V = 11
print("Minimum coins required is ", top_down_min_coin(coins, V)) 

