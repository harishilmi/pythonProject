from tabulate import tabulate

interface_list = [
    {'name': 'gi1',
     'ip': '192.168.1.1',
     'mask': '255.255.255.0'},
    {'name': 'gi2',
     'ip': '192.168.2.1',
     'mask': '255.255.255.0'},
    {'name': 'gi3',
     'ip': '192.168.3.1',
     'mask': '255.255.255.0'},
    {'name': 'gi4',
     'ip': '192.168.4.1',
     'mask': '255.255.255.0'}
]

print(tabulate(interface_list, tablefmt='fancy_grid'))

hdr = ['Name', 'IP', 'Mask']
value_list = []
for intf in interface_list:
    value_list.append(list(intf.values()))

# print(value_list)
print(tabulate(value_list, headers=hdr, tablefmt='fancy_grid'))












