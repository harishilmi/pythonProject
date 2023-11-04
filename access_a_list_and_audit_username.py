import re
from netmiko import ConnectHandler

devices = ['192.168.0.121', '192.168.0.122', '192.168.0.123']

passwd = input('Key in password: ')

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'bigg',
        'password': passwd,
        'port': 22,
        'secret': 'bigg',
        'verbose': True
        }

    connection = ConnectHandler(**cisco_device)
    print('connecting to ' + ip)
    print('entering enable mode ..')
    connection.enable()
    shrun = connection.send_command('show run')
    # print(shrun)
    shrun = shrun.splitlines()
    # print(shrun)
    shrun_idx = [i for i, item in enumerate(shrun) if re.search('^username', item)]
    for item in shrun_idx:
        print('audit item for router ' + ip + ' : ' + shrun[item] + '\n')



# with open('shrun.txt') as f:
#     shrun = f.readlines()
#
# print(shrun)
#
# shrun_idx = [i for i, item in enumerate(shrun) if re.search('^username', item)]
# print(shrun_idx)
# print(type(shrun_idx))
#
# for item in shrun_idx:
#     print('audit item: ' + shrun[item])