# Lockboxes :smile:

This Python script aims to determine whether all the given lockboxes can be opened, considering each box might contain keys to other boxes.

### Problem Description
You have `n` number of locked boxes in front of you, numbered sequentially from 0 to n - 1. Each box may contain keys to other boxes, and a key with the same number as a box opens that box. The task is to determine if all the boxes can be opened, considering the relationships between keys and boxes.

### How to Use

The script contains a function named `canUnlockAll(boxes)`, which takes a list of lists (`boxes`) as input. The `boxes` parameter represents the lockboxes and their respective keys.

Example usage in Python:
```python
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
```

### Implementation Details
The script utilizes a breadth-first search (BFS) algorithm to traverse through the boxes and their keys. It marks visited boxes and determines if all boxes can be unlocked starting from the initial unlocked box (box 0).

### File Structure
- `0-lockboxes.py`: Contains the implementation of the `canUnlockAll()` function.
- `main_0.py`: Shows example usage of the `canUnlockAll()` function with test cases.

### Running the Script
To test the functionality of the script with your own data or additional test cases, modify the `main_0.py` file or import the `canUnlockAll()` function into your Python environment.

### Dependencies
This script does not have any external dependencies.
