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
    'device_type': 'arista_eos',
    'host': '192.168.0.141',
    'username': 'bigg',
    'password': 'bigg',
    'port': 22,
    'secret': 'bigg',
    'verbose': True,
    'banner_timeout': 20
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
configs = ['interface loopback100', 'ip address 2.2.2.2 255.255.255.255']
connection.send_config_set(config_commands=configs)
# connection.send_command('ip address 2.2.2.2 255.255.255.255')
# # output = connection.send_command('sh run')
# # print(output)
# # test = output.splitlines()
# # print(test)

# connection.disconnect()