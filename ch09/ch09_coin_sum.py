

# Problem 31: Coin sums
# https://projecteuler.net/problem=31

# dynamic programming
def coin_sum(total, coins):
    ways = [1] + ([0] * total)
    for coin in coins:
        for i in range(coin, total+1):
            ways[i] += ways[i - coin]
    return ways[total]
    
def coin_sum_r(total, coins):
    if len(coins) == 1:
        return 1
    elif total < coins[-1]:
        return coin_sum_r(total, coins[:-1])
    else:
        return (coin_sum_r(total-coins[-1], coins) + 
                coin_sum_r(total, coins[:-1]))

# coins_a = (1, 5, 10, 25)   
# print(coin_sum(100, coins_a))   # 242

# coins_b = (1, 5, 10, 25, 50, 100)  
# print(coin_sum(100000, coins_b))   # 13398445413854501

coins_england = (1, 2, 5, 10, 20, 50, 100, 200)
# print(coin_sum(100, coins_england))   # 73682
# print(coin_sum(600, coins_england))   # 73682
# print(coin_sum_r(600, coins_england))   # 73682

coins_x = (1, 2)
for i in range(1, 12+1):
    print(coin_sum(i, coins_x)) 


