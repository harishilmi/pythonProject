import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# creating a dictionary for each device to connect to
router1 = {'hostname': 'router1', 'port': '22', 'username': 'bigg', 'password': 'bigg'}
router2 = {'hostname': 'router2', 'port': '22', 'username': 'bigg', 'password': 'bigg'}
router3 = {'hostname': 'router3', 'port': '22', 'username': 'bigg', 'password': 'bigg'}

# creating a list of dictionaries (of devices)
routers = [router1, router2, router3]

# iterating over the list (over the devices) and backup the config
for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n')  # this is the enable password
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)

    if ssh_client.get_transport().is_active() == True:
        print('Closing connection...')
        ssh_client.close()

