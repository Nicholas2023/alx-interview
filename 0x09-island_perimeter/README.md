# Island Perimeter :smile:

This program calculates the perimeter of an island represented by a grid.

## Description

Given a grid where 1 represents land and 0 represents water, this program calculates the perimeter of the island described in the grid. The island is completely surrounded by water and does not contain any "lakes" (water inside that isn’t connected to the water surrounding the island). The cells of the grid are square, with a side length of 1, and are connected horizontally/vertically (not diagonally).

## Function

The `island_perimeter(grid)` function takes a list of lists of integers (`grid`) as input and returns the perimeter of the island.

### Parameters

- `grid`: A list of lists of integers representing the grid where 1 represents land and 0 represents water.

### Return Value

- An integer representing the perimeter of the island.

## Usage

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Constraints

- The width and height of the grid do not exceed 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Files

- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `0-main.py`: Contains a test case to demonstrate the usage of the `island_perimeter` function.

## Author

- [Nicholas Otieno](https://github.com/Nicholas2023)
