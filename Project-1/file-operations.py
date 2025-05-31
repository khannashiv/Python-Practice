def update_server_conf(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                # Update the line with the new value
                file.write(key + '=' + value + '\n')
            else:
                # Write the line as it is
                file.write(line)

update_server_conf('server.conf', 'MAX_CONNECTIONS', '400')