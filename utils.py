import csv
from db_utils import print_query_results    # Importing function for printing results in table format

# Function to write the results to a CSV file
def write_to_csv(log_csv, activity_per_ip, most_accessed, suspicious_activity):
    """
        Writes the log analysis results to a CSV file.
        
        Arguments:
            log_csv (str): The name of the CSV file where the results will be saved.
            activity_per_ip (list): List of tuples from SQL query result containing IP address and request count.
            most_accessed (list): List of tuples from SQL query result containing endpoint and access count.
            suspicious_activity (list): List of tuples from SQL query result containing IP address and failed login count.
    """

    # Open CSV file in write mode
    with open(log_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        # Directly write the SQL query result
        writer.writerows(activity_per_ip)
        writer.writerow([])  # Blank line
        
        # Write Most Accessed Endpoint
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        # Directly write the SQL query result
        writer.writerows(most_accessed)
        writer.writerow([])  # Blank line
        
        # Write Suspicious Activity
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        # Directly write the SQL query result
        writer.writerows(suspicious_activity)

def print_in_terminal(activity_per_ip,most_accessed,suspicious_activity):
    """
        Prints the log analysis results in a table format in the terminal.
        
        Arguments:
            activity_per_ip (list): List of tuples from SQL query result containing IP address and request count.
            most_accessed (list): List of tuples from SQL query result containing endpoint and access count.
            suspicious_activity (list): List of tuples from SQL query result containing IP address and failed login count.
    """
    
    # Print Requests per IP in table format
    headers = ["IP Address", "Request Count"]
    print_query_results(activity_per_ip, headers)
    
    # Print Most Accessed Endpoint in table format
    headers = ["Endpoint", "Access Count"]
    print_query_results(most_accessed, headers)

    # Print Suspicious Activity in table format
    headers = ["IP Address", "Failed Login Count"]
    print_query_results(suspicious_activity, headers)

