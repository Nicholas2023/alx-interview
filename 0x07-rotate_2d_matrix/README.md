# Rotate 2D Matrix :smile:

## Description

This Python script provides a function to rotate an n x n 2D matrix 90 degrees clockwise in-place. The rotation is achieved by transposing the matrix and then reversing each row.

## Usage

1. Make sure you have Python 3 installed on your system.

2. Run the script using the following command:

    ```bash
    ./main_0.py
    ```

3. The script includes a test case where a sample matrix is rotated, and the result is printed to the console.

## Function

```python
def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in-place.

    :param matrix: The input matrix to be rotated.
    :type matrix: List[List[int]]
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
```

## Example

```python
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

## Output

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```
