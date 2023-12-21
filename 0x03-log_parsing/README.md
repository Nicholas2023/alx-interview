# Log Parsing Script :wink:

This script reads log data line by line from standard input and computes statistics based on the log format provided.

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your_username/log-parsing.git
    ```

2. **Navigate to the Directory:**

    ```bash
    cd log-parsing
    ```

3. **Run the Log Generator:**

    Use the provided log generator script to generate log data:

    ```bash
    ./0-generator.py | python3 0-stats.py
    ```

4. **Understanding Output:**

    - The script processes the log lines and calculates statistics every 10 lines or upon interruption (Ctrl+C).
    - Statistics include the total file size and the count of different HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).

## File Descriptions

- `0-generator.py`: Python script to generate log data in the specified format.
- `0-stats.py`: Python script for parsing log data, computing statistics, and printing results.

## Input Log Format

The input log lines should adhere to the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

## Script Details

- `0-stats.py` reads log data line by line from standard input.
- It computes and prints statistics for every 10 lines or upon interruption.
- The script calculates total file size and counts occurrences of specified HTTP status codes.

## Sample Output

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3

File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3

...
```

## Note

- This script assumes that log lines follow the specified format. Lines not conforming to this format will be skipped.
