# Bincom Staff Color Analysis Project

This project analyzes the colors worn by Bincom staff during the week and performs various statistical operations. It calculates statistics like the mean, median, and variance of the colors and stores the color frequency data in a PostgreSQL database. The project also demonstrates how to handle sensitive information like database credentials using environment variables.

## Features

1. **Color Extraction**: Extracts color data from a hardcoded table in the code.
2. **Statistical Calculations**:
    - Mean color
    - Median color
    - Variance of color frequency
    - Probability of picking "Red" at random
3. **Database Storage**: Saves color frequency data into a PostgreSQL database.
4. **Environment Variable Support**: Uses a `.env` file to securely store sensitive information like the database connection string.
5. **Bonus Features**: Includes recursive search and random binary generation.

## Project Structure

```plaintext
├── color-analyze-entry.py    # Main entry point for running the analysis
├── color_extract.py          # Extracts and normalizes color data
├── stats_calculation.py      # Calculates mean, median, variance, and probability
├── database.py               # Handles PostgreSQL connection and operations
├── .env                      # Stores sensitive information (should not be committed)
└── README.md                 # Project documentation

