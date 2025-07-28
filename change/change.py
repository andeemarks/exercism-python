def find_fewest_coins(coins: list, target):
    if target < 0:
        raise ValueError("target can't be negative")
        
    if target == 0:
        return []
 
    [best_fit_coins, dp] = populate(coins, target)

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    solution = reconstruct(target, best_fit_coins)
    
    return sorted(solution)

def reconstruct(target: int, best_fit_coins: list) -> list:
    solution = []
    current = target
    while current > 0:
        coin_used = best_fit_coins[current]
        solution.append(coin_used)
        current -= coin_used

    return solution

def populate(coins: list, target: int) -> [list, list]:
    array_lengths = target + 1
    dp = [float('inf')] * array_lengths
    dp[0] = 0
    best_fit_coins = [-1] * array_lengths  # Track which coin was used

    for amount in range(1, array_lengths):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                best_fit_coins[amount] = coin

    return [best_fit_coins, dp]
