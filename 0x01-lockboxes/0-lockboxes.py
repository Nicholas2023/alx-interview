#!/usr/bin/python3
"""
A module that implements the breadth-first search to solve algorithmic quiz
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened by traversing
    through the keys
    Args:
        boxes (list of lists): Represents the lockboxes and
        their respective keys
    Returns:
        bool: True if all boxes can be opened, else False
    """

    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
