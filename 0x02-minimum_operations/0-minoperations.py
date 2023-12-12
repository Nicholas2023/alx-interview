#!/usr/bin/env python3
"""
A module that implements the minOperations()
"""
import math


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result
    in exactly n H chars in the file
    Args:
        n (int): The target number of H characters
    Returns:
        The minimum number of operations needed to acheive n chars
        If n is impossible to acheive, return 0
    """
    # Base case
    if n == 1:
        return 0

    # Find the largest power of 2 less than or equal to n
    power = 2 ** int(math.log2(n))

    # Check if n is directlt achievable by pasting
    if n % power == 0:
        return int(math.log2(n))

    # Recursively calculate the min operation for both possibilities
    # 1. Copy all chars and paste n // power times
    # 2. Copy all chars, paste power times.

    return 1 + min(
        int(math.log2(n)) + 1,
        minOperations(n - power) + 2
    )
