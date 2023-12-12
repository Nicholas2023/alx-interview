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
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
