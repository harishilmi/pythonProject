from netmiko import ConnectHandler
from tabulate import tabulate
import re

cisco_device = {
    'device_type': 'cisco_ios',
    'host': 'router1',
    'username': 'bigg',
    'password': 'bigg',
    'port': 22,
    'secret': 'bigg',
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)
# print("!")
# prompt = connection.find_prompt()
# print(prompt)

connection.enable()

output = connection.send_command('sh ip bgp summ')
# print(output)

output = output.splitlines()
# print(output)

for index,item in enumerate(output):
    # print(index,item)
    if '192' in item:
        print(item)



# print(output)
#
# for item in output:
#     if 'Neighbor' in item:
#         print(item)