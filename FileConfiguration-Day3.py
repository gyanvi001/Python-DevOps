#Update the server configuration file when the max connection reach out to 200.

def update_server_config(file_path,key,value):
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                 file.write(key + "=" + value + "\n")
            else:
                # Keep the existing line as it is
                file.write(line)


# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value) 


