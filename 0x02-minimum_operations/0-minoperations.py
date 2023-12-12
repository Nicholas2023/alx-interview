#!/usr/bin/env python3
"""
A module that implements the minOperations()
"""


def minOperations(n: int) -> int:
    """
    Returns the minimum number of operations required to
    achieve a specific number of characters in a text
    where only 'Copy All' and 'Paste' are allowed
    """
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
