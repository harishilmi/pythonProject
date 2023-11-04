import time

import paramiko
# method = actions we are going to perform on device, execute show commands, parse output
# class name = CiscoDevice
# attributes = ip, username, password
class CiscoDevice:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = 22

    #below is the method that can be used like r1.connect()

    def connect(self):
        print(f"connecting to the device {self.ip}")
        session = paramiko.client.SSHClient()
        session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        session.connect(hostname=self.ip,
                            username=self.username,
                            password=self.password,
                            look_for_keys=False,
                            allow_agent=False)

        self.device_access = session.invoke_shell()
        self.device_access.send('terminal length 0\n')
        time.sleep(2)
        print('connected to device')

    def get_show_output(self, show_command):
        self.device_access.send(f"{show_command}\n")
        time.sleep(3)
        sh_output = self.device_access.recv(65000).decode()
        return sh_output

    def disconnect(self):
        self.device_access.close()
        print('\nClosed SSH connection')





# method is function associated to clss
# r1 = CiscoDevice('192.168.0.121', 'bigg', 'bigg')
# r2 = CiscoDevice(ip='192.168.0.122', username='bigg', password='bigg')
# #this is an instance of a cisco device class
# # print(type(r1))
# # print(dir(r1))
# # print(r1.password)
# r1.connect()
# r2.connect()



