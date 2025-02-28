# syte-test-assignment

## Overview

This project provides a set of tools for processing CSV and TSV files, including converting TSV files to CSV format and removing rows based on regex patterns.

## Features

- **TSV to CSV Conversion**: Convert TSV files to CSV format.
- **Row Filtering by Regex**: Remove rows from a CSV file that match a specific pattern and do not match another pattern.

## Requirements

- Python 3.8+
- pip

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/syte-test-assignment.git
   cd syte-test-assignment
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### TSV to CSV Conversion

To convert a TSV file to CSV format, use the `convert_tsv_to_csv` function from the `converter` module.

```sh
python src/converter.py --infile python_home_task_file.tsv
```

### Adding price_edited float column from search_price

```sh
python src/csv_task.py --infile python_home_task_file.csv --out python_home_task_file_with_price.csv
```

### Removing rows having 'knit' without 'jumpers'

```sh
python src/regex_task.py --infile python_home_task_file.csv --out python_home_task_file_regex.csv
```
