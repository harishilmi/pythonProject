import re
from netmiko import ConnectHandler

devices = ['192.168.0.121', '192.168.0.122', '192.168.0.123']

for ip in devices:

    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'bigg',
        'password': 'bigg',
        'port': 22,
        'secret': 'bigg',
        'verbose': True
        }

    connection = ConnectHandler(**cisco_device)
    # print('entering enable_mode..')
    connection.enable()

    output = connection.send_command('show ver')
    version_Regex = re.compile('[A-Za-z]+ \d\d\.\d\([0-9]+\)[A-Za-z]+\d')

    needed_version = version_Regex.search(output)
    print('getting version from router... ')
    print('The version of ' + ip + ' is ' + needed_version.group() + '\n')