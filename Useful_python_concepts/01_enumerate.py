### enumerate

vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme']
search = vendors.index('cumulus')
print(search)

e = enumerate(vendors)
print(e)

for data in enumerate(vendors, start=1):
    print(data)

for index,name in enumerate(vendors):
    print(index, name)

for index, name in enumerate(vendors):
    if 'ext' in name:
        print(vendors[index])