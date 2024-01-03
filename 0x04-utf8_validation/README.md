# UTF-8 Validation :smile:

This Python script checks whether a given list of integers represents a valid UTF-8 encoding according to UTF-8 standards.

## Task Description

Write a method (`validUTF8`) that determines if a given data set represents a valid UTF-8 encoding.

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data; hence, we only need to handle the 8 least significant bits of each integer.

## Implementation Details

The `validUTF8` function within the Python script iterates through the given list of integers representing bytes and validates if they constitute a valid UTF-8 encoding. It performs the following steps:

1. Counts the number of leading ones in the byte to determine the character's byte length.
2. Validates the sequence of bytes based on UTF-8 rules:
   - Characters starting with 0 (1-byte character) are validated.
   - Characters starting with a specific number of leading ones (2, 3, or 4) are checked for proper following byte format (which must start with `10`).

## Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the directory containing the script:

   ```bash
   cd 0x04-utf8_validation
   ```

3. Run the main script:

   ```bash
   python3 0-validate_utf8.py
   ```

## Example

Given test cases:

```python
data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Output: False
```

## Contributors

- [@Nicky Mane](https://github.com/Nicholas2023)
