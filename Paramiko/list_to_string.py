routers = ['router1', 'router2', 'router3']

for router in routers:
    print(router)

print(routers)

routerstring = '\n'.join(routers)

print(routerstring)

with open('routerlist.txt', 'w') as f:
    f.write(routerstring)