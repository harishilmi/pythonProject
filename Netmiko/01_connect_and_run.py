# netmiko makes it simpler but does not support all platform
# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': 'router1',
       'username': 'u1',
       'password': 'bigg',
       'port': 22,             # optional, default 22
       'secret': 'bigg',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# sending a command and getting the output
output = connection.send_command('sh ip int brief')
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()