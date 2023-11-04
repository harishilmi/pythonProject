from operator import itemgetter

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

# dict_getter = itemgetter('ip', 'name')
# print(dict_getter)
#
# # print(dict_getter(interface_list[1]))
#
# for interface in interface_list:
#     print(dict_getter(interface))

vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme']
list_getter = itemgetter(2)
print(list_getter(vendors))

for vendor in vendors:
    print(list_getter(vendor))


















# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# print(type(thisdict))