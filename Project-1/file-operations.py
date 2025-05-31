def update_server_conf(file_path, key, value):
    """
    Updates a specific key-value pair in a configuration file.
    If the key exists in the file, its value is updated.
    If the key is not found, it is NOT added to the file.
    
    Args:
        file_path (str): Path to the configuration file.
        key (str): Configuration key to update.
        value (str): New value for the key.
    """

    # Open the file in read mode to get all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

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
update_server_conf('server.conf', 'MAX_CONNECTIONS', '400')