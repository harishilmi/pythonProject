from napalm import get_network_driver
import json
import pprint

driver = get_network_driver('nxos')

optional_args = {'secret': 'bigg' } #enable password
nxos = driver('192.168.0.151', 'bigg', 'bigg', optional_args=optional_args)
nxos.open()


output = nxos.get_arp_table()
print(output)

print(type(output))
print('***** make it nicer *****')

dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)
print(type(dump))

with open('interface_nxos.txt', 'w') as f:
    f.write(dump)

# output2 = nxos.get_interfaces_counters()
# dump2 = json.dumps(output2, indent=4)
# print(dump2)

nxos.close()