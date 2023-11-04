from operator import itemgetter
### sorted() - Function and sort() method

vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme']
print(sorted(vendors, reverse=True))
vendors.sort()
print(vendors)

'''key based sorting'''

interface_list = [
    {'name': 'gi1',
     'ip': '192.168.1.1',
     'mask': '255.255.255.0'},
    {'name': 'gi2',
     'ip': '192.168.2.1',
     'mask': '255.255.255.0'},
    {'name': 'gi3',
     'ip': '192.168.0.1',
     'mask': '255.255.255.0'},
    {'name': 'gi4',
     'ip': '192.168.4.1',
     'mask': '255.255.255.0'}
]

dict_getter = itemgetter("ip")
print(sorted(interface_list, key=dict_getter))