from log_parser import log_parser
from db_utils import *  # Utility functions for database operations
from utils import * # Utility functions for writing to CSV and terminal display



# Global variables for the log file, database file, and output CSV
log_file = "sample.log"            # Path to the log file to be processed
db_file = "log_analysis.db"        # Database file to store logs
log_csv = "log_analysis_results.csv"  # Output CSV file name for storing results
DEBUG = True                      # Flag to toggle debug mode for terminal printing



def main():
    """
        Main function to start the log analysis process.
            - Reads the log file
            - Inserts parsed logs into the database
            - Fetches data for analysis
            - Writes results to a CSV file
            - Display results on terminal
    """
    # Setup the database connection
    conn = setup_database(db_file)   # Initialize database
    cursor = conn.cursor()           # Create a cursor to interact with the database
    
    print("Logs read start")

    # Open and read the log file line by line
    with open(log_file,'r') as logs:
        for log in logs:
            try:    
                # Parse each log entry using the log_parser function
                log_verdict = log_parser(log.strip())

                # Insert parsed log data into database
                insert_log(cursor,log_verdict)

            except Exception as e:
                print("Error =>",e)

    # Commit the changes to the database (to save all the inserted logs)
    conn.commit()
   

    # Fetch analyzed data from the database for further processing

    # Get request counts per IP
    activity_per_ip = get_activity_per_ip(cursor)
    # Get most accessed endpoints
    most_accessed = get_most_freq_accessed_resource(cursor)
    # Get suspicious login attempts
    suspicious_activity = get_suspicious_activity(cursor)
        
    # Write the fetched data to a CSV file
    write_to_csv(log_csv,activity_per_ip, most_accessed, suspicious_activity)
    
    # If DEBUG is True, print the results to the terminal
    if DEBUG :
        print_in_terminal(activity_per_ip,most_accessed,suspicious_activity)

    # Close the database connection after all operations are complete
    conn.close()

    print("Log analysis Done.")

if __name__ == "__main__": 
    main()