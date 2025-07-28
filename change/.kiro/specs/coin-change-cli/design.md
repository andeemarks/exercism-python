# Design Document

## Overview

The coin change CLI function will implement a dynamic programming solution to solve the classic coin change problem. The system will consist of a core algorithm function, input validation, CLI interface, and comprehensive error handling. The solution will use bottom-up dynamic programming to find the minimum number of coins and backtracking to reconstruct the actual coin combination.

## Architecture

The system will be structured with the following components:

1. **Core Algorithm Module**: Contains the main coin change logic
2. **Validation Module**: Handles input validation and error checking
3. **CLI Interface**: Provides command-line access to the functionality
4. **Error Handling**: Custom exceptions and error messages

## Components and Interfaces

### Core Algorithm Component

**Function**: `find_fewest_coins(coins, target)`
- **Input**: 
  - `coins`: List of positive integers representing coin denominations
  - `target`: Non-negative integer representing the target amount
- **Output**: List of integers representing the coins used to make change
- **Algorithm**: Dynamic programming with backtracking
  - Use DP array to find minimum coins needed for each amount from 0 to target
  - Use parent array to track which coin was used for each amount
  - Backtrack from target to reconstruct the solution

### Validation Component

**Function**: `validate_inputs(coins, target)`
- Validates coin denominations are positive integers
- Validates target is non-negative integer
- Validates coins list is not empty
- Raises appropriate ValueError with descriptive messages

### CLI Interface Component

**Function**: `main()`
- Parses command line arguments using argparse
- Calls validation and core algorithm
- Formats and displays results
- Handles exceptions and displays user-friendly error messages

**Command Line Format**:
```
python change.py --coins 1 5 10 25 --target 67
python change.py -c 1 5 10 25 -t 67
```

## Data Models

### Input Data
- `coins`: List[int] - Valid coin denominations (positive integers)
- `target`: int - Target amount for change (non-negative integer)

### Output Data
- `result`: List[int] - List of coins that sum to target amount, using minimum number of coins

### Internal Data Structures
- `dp`: List[int] - Dynamic programming array storing minimum coins needed for each amount
- `parent`: List[int] - Array storing which coin denomination was used for each amount
- `coin_used`: List[int] - Array storing the actual coin value used for each amount

## Error Handling

### Custom Exceptions
- Utilize built-in `ValueError` for input validation errors

### Error Scenarios
1. **Negative coin denominations**: Raise ValueError with message "coin denominations must be positive"
2. **Negative target amount**: Raise ValueError with message "target can't be negative"
3. **Empty coin list**: Raise ValueError with message "can't make target with given coins"
4. **Zero in coin denominations**: Raise ValueError with message "coin denominations must be positive"
5. **Impossible target**: Raise ValueError with message "can't make target with given coins"

### CLI Error Handling
- Catch and display validation errors with helpful messages
- Provide usage information for invalid command line arguments
- Exit gracefully with appropriate exit codes

## Algorithm Details

### Dynamic Programming Approach
1. Initialize DP array where `dp[i]` represents minimum coins needed for amount `i`
2. Initialize parent tracking arrays for solution reconstruction
3. For each amount from 1 to target:
   - For each coin denomination:
     - If coin <= current amount and using this coin gives fewer total coins:
       - Update dp[amount] and parent tracking
4. If target amount is unreachable, raise exception
5. Backtrack using parent arrays to reconstruct solution

### Time Complexity: O(target × len(coins))
### Space Complexity: O(target)

## Testing Strategy

### Unit Tests
1. **Valid Input Tests**:
   - Standard cases with common coin denominations
   - Edge case: target = 0 (should return empty list)
   - Cases with multiple optimal solutions
   - Large target amounts with small denominations

2. **Error Condition Tests**:
   - Negative coin denominations
   - Negative target amounts
   - Empty coin list
   - Zero in coin denominations
   - Impossible targets

3. **CLI Integration Tests**:
   - Valid command line arguments
   - Invalid command line arguments
   - Help message display
   - Error message formatting

### Test Data Examples
- coins=[1, 5, 10, 25], target=67 → expected result uses minimum coins
- coins=[2, 4], target=3 → should raise exception (impossible)
- coins=[1], target=0 → should return []
- coins=[-1, 5], target=10 → should raise ValueError