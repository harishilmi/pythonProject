from napalm import get_network_driver
import json
import pprint

driver = get_network_driver('ios')

optional_args = {'secret': 'bigg' } #enable password
ios = driver('192.168.0.121', 'bigg', 'bigg', optional_args=optional_args)
ios.open()


output = ios.get_arp_table()
print(output)

print(type(output))

print('***** make it nicer *****')
for item in output:
    print(item)
print(dir(ios))


ios.close()