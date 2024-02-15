# Prime Game :smile:

## Description
Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n, and removing that number and its multiples from the set. The player who cannot make a move loses the game. They play multiple rounds of the game with different ranges of integers for each round. Given the number of rounds and the ranges for each round, the task is to determine the winner of each game.

## Function Signature
```python
def isWinner(x, nums):
    pass
```

## Parameters
- `x`: An integer representing the number of rounds to play.
- `nums`: An array of integers representing the range of integers for each round.

## Returns
- The name of the player who won the most rounds.
- If the winner cannot be determined, returns `None`.

## Constraints
- The values of `x` and `nums` will not be larger than 10000.

## Example
```python
x = 5
nums = [2, 5, 1, 4, 3]
print("Winner: {}".format(isWinner(x, nums)))  # Output: "Ben"
```

## Approach
1. Define a helper function `is_prime` to check if a number is prime.
2. Define another helper function `find_next_prime` to find the next prime number starting from a given integer.
3. Iterate through each round specified in `nums`.
4. Play the game according to the rules described, keeping track of the winner of each round.
5. Determine the overall winner based on the number of wins for each player.
```
