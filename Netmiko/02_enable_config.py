# from netmiko import Netmiko
#
# connection = Netmiko(host='router1', port='22', username='bigg', password='bigg', secret='bigg', device_type='cisco_ios')
#
# # print(connection.send_command('sh interface'))
#
# output = connection.send_command('sh inter')
# print(output)

from netmiko import ConnectHandler

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
print("!")
prompt = connection.find_prompt()
print(prompt)

connection.enable()

prompt = connection.find_prompt()
print("!")
print(prompt)
print("!")
connection.config_mode()
prompt = connection.find_prompt()
print(prompt)
# connection.send_command('int lo200')
# output = connection.send_command('sh run')
# print(output)
# test = output.splitlines()
# print(test)

# connection.disconnect()