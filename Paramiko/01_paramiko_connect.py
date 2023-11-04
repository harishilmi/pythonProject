import paramiko

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to router1')
ssh_client.connect(hostname='router1', port='22', username='bigg', password='bigg',
                   look_for_keys=False, allow_agent=False)


# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
# ...

print('Closing connection')
ssh_client.close()