# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Function to get the server status and port
def get_server_info(server_name):
    # Get the server config or return a default if the server is not found
    server = server_config.get(server_name, {})
    
    # Retrieve 'status' and 'port' with default values if not found
    status = server.get('status', 'Status not found')
    port = server.get('port', 'Port not found')
    
    return status, port

# Example usage
server_info = get_server_info('server3')
print(f"Server3 status and port number: {server_info}")

########################### Summary ##########################

# How It Works in this context ?

    # If server_name exists in server_config, the corresponding server details (like 'ip', 'port', 'status') will be returned as the value for that key.
    # If server_name does not exist, {} (an empty dictionary) will be returned instead, 
    # and you can safely attempt to retrieve values from this empty dictionary later in the code (without causing any errors).

################## PRACTICE ##################################

# print(server_config)
# print(server_config['server1'])  # This will print the configuration of server1, which includes its IP, port, and status.
# print(server_config.get('server2'))  # This will retrieve the configuration of server2, returning None if it does not exist.
# print(server_config.get('server4'))  # This will attempt to retrieve server4's configuration, returning 'Server not found' if it does not exist.
# print(server_config.get('server1').get('ip')) # This will retrieve the IP address of server1.
 
################## GET Function in Python ######################

# About the get() function in Python.

    # In Python, the get() function is used with dictionaries to retrieve the value associated with a specified key.
    # It has a key advantage over direct dictionary access (dict[key]): if the key doesn't exist, get() returns None or a default value instead of raising a KeyError.

        #  For Example : my_dict = {"name": "Shiv", "age": 25}

            #     print(my_dict.get("name"))  # Output: Shiv
            #     print(my_dict.get("city"))  # Output: None (since "city" isn't in the dictionary)
            #     print(my_dict.get("city", "Unknown"))  # Output: Unknown (providing a default value)

####################################################################