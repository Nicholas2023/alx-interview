# Minimum Operations :wink:

This task involves calculating the minimum number of operations required to achieve a specific number of characters ('H') in a text file using only 'Copy All' and 'Paste' operations.

### Problem Description

Given a number `n`, the task is to find the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

### Method

The implemented method `minOperations(n)` follows this logic:
- If `n` is less than or equal to 1, returns 0 (no operations needed).
- It iterates through the factors of `n`, counting each factor to the operations.
- Finally, if `n` is still greater than 1 after the loop, it adds `n` itself to the operations count.

### Usage

The function `minOperations(n)` takes an integer `n` as input and returns the minimum number of operations required.

### Example

```python
n = 9
print("Min # of operations to reach {} chars: {}".format(n, minOperations(n)))  # Output: 6

n = 12
print("Min # of operations to reach {} chars: {}".format(n, minOperations(n)))  # Output: 7
```

### Execution

Execute the provided `minOperations` function with the desired integer `n` to determine the minimum number of operations required to generate `n` 'H' characters.
