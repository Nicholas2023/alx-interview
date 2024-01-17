# Star Wars API - Characters Script :smile:

This script fetches and displays the characters of a specified Star Wars movie using the Star Wars API.

## Prerequisites

Before running the script, make sure you have Node.js installed on your machine. You will also need to install the `request` module.

```bash
npm install request
```

## Usage

To run the script, use the following command:

```bash
node 0-starwars_characters.js <Movie ID>
```

Replace `<Movie ID>` with the desired Star Wars movie ID.

### Example

```bash
node 0-starwars_characters.js 3
```

## Script Explanation

The script utilizes the Star Wars API to fetch the characters for a specified movie and then prints their names one per line in the order they appear in the API response.

## Files

- **0-starwars_characters.js**: The main script file.
- **package.json**: Configuration file for Node.js dependencies.

## Credits

This script is part of the ALX-Interview GitHub repository.
