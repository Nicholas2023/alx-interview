# N-Queens Problem Solver :smile:

This Python script solves the N-Queens problem using a backtracking algorithm. The N-Queens problem is the challenge of placing N non-attacking queens on an N×N chessboard.

## Usage

### Running the Script

Make sure you have Python installed. The script `0-nqueens.py` takes one argument `N`, where `N` is an integer greater than or equal to 4.

```bash
./0-nqueens.py N
```

### Example

```bash
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Implementation Details

The script uses a backtracking algorithm to find and print all possible solutions for the N-Queens problem. It checks for valid queen placements by ensuring that no two queens threaten each other along the rows, columns, or diagonals on the chessboard.

## File Structure

- `0-nqueens.py`: Python script to solve the N-Queens problem
- `README.md`: This documentation file

## Requirements

- Python 3.x

## Note

- The script only uses the `sys` module for argument handling.
