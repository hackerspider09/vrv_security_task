import sqlite3

# Default database file name
db_file = "log_analysis.db" 

# Initialize SQLite database
def setup_database(db_file_name):
    """
        Initializes the SQLite database by creating the necessary table for storing logs.
        It also drops the 'logs' table if it exists, to start fresh.
        
        Arguments:
            db_file_name (str): The name of the SQLite database file.
        
        Returns:
            conn (sqlite3.Connection): The database connection object.
    """
    global db_file
    db_file = db_file_name  # Set global db_file variable

    # Connect to SQLite db and create cursor for executing SQL commands
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()

    # Drop the logs table if it exists (clears old data)
    cursor.execute('DROP TABLE IF EXISTS logs')

    # Create table for storing logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            date TEXT,                             
            time TEXT,                            
            ip_address TEXT,                     
            status_code INTEGER,                 
            size INTEGER,                        
            method TEXT,                         
            resource TEXT,                       
            error TEXT                          
        )
    ''')

    # Commit the changes to create table
    conn.commit()

    return conn

# Insert log into database
def insert_log(cursor, log_data):
    """
        Inserts a log entry into the 'logs' table in the SQLite database.
        
        Arguments:
            cursor (sqlite3.Cursor): The cursor to execute the SQL query.
            log_data (dict): Dictionary containing log data to be inserted.
    """
    try:
        # Execute SQL command to insert data
        cursor.execute('''
            INSERT INTO logs (date, time, ip_address, status_code, size, method, resource, error)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            log_data["date"],
            log_data["time"],
            log_data["ip_address"],
            log_data["status_code"],
            log_data["size"],
            log_data["method"],
            log_data["resource"],
            log_data["error"]
        ))
    except sqlite3.Error as e:
        print(f"Error inserting log into database: {e}")

def print_row(rows):
    """
        Prints the rows of data to the console.
        
        Arguments:
            rows (list): List of tuples representing rows of data.
    """
    for row in rows:
        print(row)

def get_activity_per_ip(cursor):
    """
        Retrieves the number of requests made by each IP address from the logs.
        
        Arguments:
            cursor (sqlite3.Cursor): The cursor to execute the SQL query.
        
        Returns:
            rows (list): List of tuples containing IP addresses and their respective request counts.
    """
    cursor.execute("SELECT ip_address,count(ip_address) as request_count FROM logs group by ip_address order by request_count desc")
    rows = cursor.fetchall()    # Fetch all results from the query
    # print_row(rows)

    return rows

def get_most_freq_accessed_resource(cursor):
    """
        Retrieves the most frequently accessed resources (endpoints) from the logs.
        
        Arguments:
            cursor (sqlite3.Cursor): The cursor to execute the SQL query.
        
        Returns:
            rows (list): List of tuples containing resources and their respective access counts.
    """
    cursor.execute("SELECT resource,count(resource) as accessed_count FROM logs group by resource order by accessed_count desc")
    rows = cursor.fetchall()    # Fetch all results from the query
    # print_row(rows)

    return rows

def get_suspicious_activity(cursor):
    """
        Retrieves IP addresses that have made more than a certain number of failed login attempts (status code 401).
        
        Arguments:
            cursor (sqlite3.Cursor): The cursor to execute the SQL query.
        
        Returns:
            rows (list): List of tuples containing IP addresses and the number of failed login attempts.
    """
    # cursor.execute("SELECT ip_address,count(status_code) as failed_accessed FROM logs group by status_code,ip_address having status_code in (401) order by failed_accessed desc") # To get only failed requests
    cursor.execute("SELECT ip_address,SUM(CASE WHEN status_code = 401 THEN 1 ELSE 0 END) AS failed_accessed FROM logs GROUP BY ip_address ORDER BY failed_accessed DESC")
    rows = cursor.fetchall()    # Fetch all results from the query
    # print_row(rows)

    return rows

    
def print_query_results(rows, headers):
    """
        Prints SQL query results in a table-like format in the console with tab-separated columns.
        
        Arguments:
            rows (list): List of tuples representing query result rows.
            headers (list): List of column headers to be printed.
    """
    # Calculate the initial column widths based on the length of each header
    column_widths = [len(header) for header in headers]
    # print(column_widths)  # Debug: Print initial column widths for verification

    # Iterate through each row to adjust column widths based on the length of the data
    for row in rows:
        for i, value in enumerate(row):
            # Update the column width to be the maximum of the current width and the length of the current value
            column_widths[i] = max(column_widths[i], len(str(value)))


    # Print the header row, with each column left-aligned and spaced according to column widths
    print("\t".join([header.ljust(column_widths[i]) for i, header in enumerate(headers)]))

    # Print each data row, with values left-aligned and spaced according to column widths
    for row in rows:
        print("\t".join([str(value).ljust(column_widths[i]) for i, value in enumerate(row)]))
