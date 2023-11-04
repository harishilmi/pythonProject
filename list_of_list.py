with open('devices.txt') as f:
    content = f.read().split()
    print(content)
    f.seek(0)
    content = f.read().splitlines()
    devices = list()
    for line in content:
        devices.append(line.split(':'))

    print(devices)

    devices = devices[1:]
    print('!')
    for device in devices:
        print(f'pinging {device[1]}')


print('*' * 100)

f = open('routers.txt')

for line in f:
    print(line, end ='')