

def coin_sum_r(total, coins):
    if len(coins) == 1:
        return 1
    elif total < coins[-1]:
        return coin_sum_r(total, coins[:-1])
    else:
        return coin_sum_r(total-coins[-1], coins) + coin_sum_r(total, coins[:-1])

coins_a = (1, 5, 10, 25)   
print(coin_sum_r(100, coins_a))   # 242

coins_england = (1, 2, 5, 10, 20, 50, 100, 200)
print(coin_sum_r(200, coins_england))   # 73682




