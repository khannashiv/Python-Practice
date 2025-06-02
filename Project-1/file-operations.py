# Description:

#     This script provides a utility function to update the value of a specific key in a configuration file.
#     The configuration file i.e. server.conf is expected to contain key-value pairs, typically in the format 'key = value'.
# Functionality:
#     - Reads all lines from the given configuration file.
#     - Searches for the specified key in each line.
#     - If the key is found in a line, replaces the entire line with the updated key-value pair.
#     - Writes all lines (updated or unchanged) back to the file, preserving the original structure except for the updated key.

def update_server_conf(file_path, key, value):
    # Open the file in read mode to get all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines from file object and store them in a list where each line is an element.

    # Open the file in write mode to update or rewrite lines
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                # Update the line with the new key-value pair
                # Alternative: file.write(key + '=' + value + '\n')  # String concatenation method
                file.write(f"{key} = {value}\n")  # Using f-string for better readability
            else:
                # Write the line as it is (preserving original content)
                file.write(line)

# Example Usage
update_server_conf('server.conf', 'MAX_CONNECTIONS', '450')