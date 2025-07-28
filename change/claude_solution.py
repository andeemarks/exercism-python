def min_coin_change(coins, target):
    """
    Calculate the minimum number of coins needed to make a target amount.
    
    Args:
        coins (list): List of available coin denominations (positive integers)
        target (int): Target amount to make change for (non-negative integer)
    
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
    
    Raises:
        ValueError: If coins contains non-positive values or target is negative
    """
    # Input validation
    if target < 0:
        raise ValueError("Target amount cannot be negative")
    
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Coin denominations must be positive integers")
    
    # Base case: no change needed
    if target == 0:
        return 0
    
    # Initialize DP array
    # dp[i] represents minimum coins needed to make amount i
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # 0 coins needed to make amount 0
    
    # Fill the DP table
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result (-1 if impossible, otherwise minimum coins needed)
    return dp[target] if dp[target] != float('inf') else -1


def min_coin_change_with_solution(coins, target):
    """
    Calculate minimum coins needed and return the actual coin combination.
    
    Args:
        coins (list): List of available coin denominations
        target (int): Target amount to make change for
    
    Returns:
        tuple: (min_coins_count, coin_combination) or (-1, []) if impossible
    """
    # Input validation (same as above)
    if target < 0:
        raise ValueError("Target amount cannot be negative")
    
    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("Coin denominations must be positive integers")
    
    if target == 0:
        return (0, [])
    
    # DP array and parent tracking
    dp = [float('inf')] * (target + 1)
    parent = [-1] * (target + 1)  # Track which coin was used
    dp[0] = 0
    
    # Fill DP table with parent tracking
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                parent[amount] = coin
    
    # If impossible to make target amount
    if dp[target] == float('inf'):
        return (-1, [])
    
    # Reconstruct solution
    solution = []
    current = target
    while current > 0:
        coin_used = parent[current]
        solution.append(coin_used)
        current -= coin_used
    
    return (dp[target], sorted(solution, reverse=True))


# Example usage and test cases
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 5, 10, 25], 30),  # Standard US coins for 30 cents
        ([1, 3, 4], 6),        # Should use [3, 3] = 2 coins
        ([2], 3),              # Impossible case
        ([1, 2, 5], 11),       # Should use [5, 5, 1] = 3 coins
        ([1], 0),              # Edge case: target = 0
        ([4, 5], 27),              # Edge case: target = 0
    ]
    
    print("=== Coin Change Calculator Results ===\n")
    
    for coins, target in test_cases:
        print(f"Coins: {coins}, Target: {target}")
        
        # Test minimum coins function
        min_coins = min_coin_change(coins, target)
        print(f"Minimum coins needed: {min_coins}")
        
        # Test function with solution
        count, solution = min_coin_change_with_solution(coins, target)
        if count != -1:
            print(f"Coin combination: {solution}")
            print(f"Verification: {sum(solution)} = {target}")
        else:
            print("No solution possible")
        
        print("-" * 40)
    
    # Interactive example
    print("\n=== Interactive Example ===")
    try:
        # US coin denominations
        us_coins = [1, 5, 10, 25]
        amount = 67
        
        count, solution = min_coin_change_with_solution(us_coins, amount)
        print(f"Making change for {amount} cents:")
        print(f"Minimum coins: {count}")
        print(f"Solution: {solution}")
        
        # Count each denomination
        from collections import Counter
        coin_count = Counter(solution)
        print("Breakdown:")
        for coin in sorted(coin_count.keys(), reverse=True):
            coin_name = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
            print(f"  {coin_count[coin]} {coin_name.get(coin, f'{coin}-cent coins')}")
            
    except ValueError as e:
        print(f"Error: {e}")