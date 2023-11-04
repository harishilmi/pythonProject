from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.121',
    'username': 'bigg',
    'password': 'bigg',
    'port': 22,  # optional, default 22
    'secret': 'bigg',  # this is the enable password
    'verbose': True  # optional, default False
    }

connection = ConnectHandler(**cisco_device)
print('entering enable mode ...')
connection.enable()

output = connection.send_command('show run')

with open('shrun.txt', 'w') as f:
    f.write(output)