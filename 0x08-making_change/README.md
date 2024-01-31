# Making Change :smile:

## Description
A Python implementation of a function to determine the fewest number of coins needed to meet a given amount total, using dynamic programming.

## Task
Given a pile of coins of different values, the task is to find the fewest number of coins needed to make a specified total amount.

## Function Signature
```python
def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given total amount.

    Parameters:
    - coins (list): List of coin values available.
    - total (int): The target total amount.

    Returns:
    - int: Fewest number of coins needed. Returns -1 if the total cannot be met.
    """
    pass
```

## Constraints
- If the total is 0 or less, the function returns 0.
- If the total cannot be met by any number of coins available, the function returns -1.
- The value of a coin will always be an integer greater than 0.
- You can assume you have an infinite number of each denomination of coin in the list.

## Example Usage
```python
makeChange([1, 2, 25], 37)
# Output: 7

makeChange([1256, 54, 48, 16, 102], 1453)
# Output: -1
```

## Implementation Details
The solution uses dynamic programming to build up a table (`dp`) where `dp[i]` represents the minimum number of coins needed to make the amount `i`. The final result is stored in `dp[total]`. If `dp[total]` is still infinity after the iteration, it means the total cannot be achieved with the given coins, and the function returns -1.

## How to Run Tests
Execute the provided test script:
```bash
./0-main.py
```
