
# Log Analysis Tool

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Why Use a Database for Log Analysis?](#why-use-a-database-for-log-analysis)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Output](#output)


## Overview
The **Log Analysis Tool** is a Python-based application designed to parse server logs, analyze data, and generate structured outputs. The tool stores log entries in a SQLite database, processes the data to extract insights, and exports the results into a CSV file. This tool is optimized for handling large-scale log data efficiently.



## Features
- **Log Parsing**: Parses raw log data and extracts key fields such as IP address, resource accessed, status codes, and timestamps.
- **Database Storage**: Stores parsed log data in an SQLite database for structured querying.
- **Data Analysis**: 
  - Counts requests per IP address.
  - Identifies the most frequently accessed endpoints.
  - Detects suspicious activities (e.g., failed login attempts).
- **CSV Export**: Outputs results in a structured CSV format.
- **Terminal Display**: Option to print results in a tabular format in the terminal.



## Why Use a Database for Log Analysis?

### Problem with Memory-Based Techniques
- **Memory Constraints**: Memory-based techniques (e.g., using Python dictionaries, lists, or Pandas) are limited by the system's RAM. Processing millions of log entries can result in crashes or slow performance due to excessive memory consumption.
- **Scalability Issues**: As the size of log data increases, the time taken for in-memory computations grows significantly, making the approach unsuitable for real-world production systems.
- **Complex Operations**: Handling operations like grouping, filtering, or aggregations in memory requires extensive coding and manual optimizations.



### Why Not Use Other Tools?
- **In-Memory Structures**: These are inefficient for large-scale logs due to memory constraints.
- **File-Based Processing**: Parsing logs directly from files is feasible for small datasets, but for large-scale data, there are slow I/O operations and a lack of efficient querying.

***This approach balances simplicity, efficiency, and scalability, making it the optimal choice for this task.***


## Requirements
- Python 3.8 or above
- SQLite (built-in with Python)
- Required Python libraries:
  - `re` (for regex-based parsing)
  - `datetime` (for timestamp handling)
  - `sqlite3` (for database interactions)
  - `csv` (for exporting results)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/hackerspider09/vrv_security_task.git
   ```
2. Navigate to the project directory:
   ```bash
   cd vrv_security_task
   ```

## Usage
1. Prepare your log file and place it in the root directory. Update the `log_file` variable in `main.py` if necessary.
2. Run the script:
   ```bash
   python3 main.py
   ```
3. Results will be displayed in the terminal (if `DEBUG = True`) and saved in a CSV file (`log_analysis_results.csv`).

### Configuration
- **Log File**: Update the `log_file` variable in `main.py` with the path to your log file.
- **Database**: The SQLite database file is defined in `db_file`. Default: `log_analysis.db`.
- **Debug Mode**: Enable debug mode to print results to the terminal by setting `DEBUG = True` in `main.py`.

## Project Structure
```
log-analysis-tool/
│
├── main.py                  # Entry point for the application
├── log_parser.py            # Module for parsing raw log entries
├── db_utils.py              # Database utility functions
├── utils.py                 # CSV writing and terminal display utilities
├── log_analysis.db          # SQLite database file (generated dynamically)
├── sample.log               # Sample log file
├── log_analysis_results.csv # Generated CSV output
└── README.md                # Project documentation
```

## Output
1. **CSV File**: Results are saved in `log_analysis_results.csv` with the following structure:
    - **log_analysis_results.csv**:
        ```
        Requests per IP
        IP Address,Request Count
        203.0.113.5,8
        198.51.100.23,8
        192.168.1.1,7
        10.0.0.2,6
        192.168.1.100,5

        Most Accessed Endpoint
        Endpoint,Access Count
        /login,13
        /home,5
        /about,5
        /dashboard,3
        /register,2
        /profile,2
        /feedback,2
        /contact,2

        Suspicious Activity
        IP Address,Failed Login Count
        203.0.113.5,8
        192.168.1.100,5
        198.51.100.23,0
        192.168.1.1,0
        10.0.0.2,0
        ```

2. **Terminal Output**: Results are displayed in a tabular format (if `DEBUG = True`).

    - **Requests per IP**:
         ```
        IP Address      Request Count
        203.0.113.5     8
        198.51.100.23   8
        192.168.1.1     7
        10.0.0.2        6
        192.168.1.100   5
        ```
    - **Most Accessed Endpoint**:
        ```
        Endpoint        Access Count
        /login  13
        /home   5
        /about  5
        /dashboard      3
        /register       2
        /profile        2
        /feedback       2
        /contact        2
        ```
    - **Suspicious Activity**:
        ```
        IP Address      Failed Login Count
        203.0.113.5     8
        192.168.1.100   5
        198.51.100.23   0
        192.168.1.1     0
        10.0.0.2        0
        ```

---

