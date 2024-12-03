import re
from datetime import datetime


def log_parser(log):
    """
        Parse a single log entry and return a dictionary with the relevant details.
        
        Args:
            log (str): A single log entry as a string.

        Returns:
            dict: Parsed log details as a dictionary.
    """

    # print(log)    # Debug purpose

    # Extract IP address
    ip_address = re.search(r".* - -", log).group(0).replace(" - -","")

    # Extract status code and size
    statusCode_size = re.search(r"(\d{3}) (\d+)",log)
    status_code = statusCode_size.group(1)
    size = statusCode_size.group(2)

    # Extract timestamp
    time_stamp = re.search(r"\[.*\]",log).group(0).split(" ")[0].replace("[","")
    parsed_time_stamp = datetime.strptime(time_stamp, "%d/%b/%Y:%H:%M:%S")

    # Extract HTTP request method and resource

    # user_request_match = re.search(r'"(GET|POST|PUT|DELETE|PATCH).*"',log)
    # user_request = user_request_match.group(0).replace('"','').split(" ")
    
    user_request_match = re.findall(r'"(.*?)"', log)
    user_request = user_request_match[0].split(" ")

    # Get error message, if available
    try:
        error_message = user_request_match[1]
    except:
        error_message = "N/A"

    # Create and return log dictionary
    log_dict = {
        "date" : parsed_time_stamp.strftime("%d/%b/%Y"),
        "time" : parsed_time_stamp.strftime("%H:%M:%S"),
        "ip_address" : ip_address,
        "status_code" : int(status_code),
        "size" : size,
        "method" : user_request[0],
        "resource" : user_request[1],
        "error" : error_message
    }

    return log_dict