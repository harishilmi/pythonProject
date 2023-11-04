import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)

router = {'server_ip':'router1', 'server_port': '22', 'user': 'bigg', 'passwd': 'bigg'}
client = myparamiko.connect(**router)
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'terminal length 0')
myparamiko.send_command(shell, 'enable')
myparamiko.send_command(shell, 'bigg')  # this is the enable command
myparamiko.send_command(shell, 'show run')

output = myparamiko.show(shell)
# processing the output
# print(output)
output_list = output.splitlines()
output_list = output_list[11:-1]
print(output_list)
output = '\n'.join(output_list)
# print(output)

file_name = 'router.txt'
print(file_name)

# writing the backup to the file
with open(file_name, 'w') as f:
    f.write(output)

myparamiko.close(client)
