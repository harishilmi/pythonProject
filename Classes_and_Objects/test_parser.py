from cisco_parser import CiscoDevice

r1 = CiscoDevice(ip='router1', username='bigg', password='bigg')

r1 = CiscoDevice(ip='router1', username='bigg', password='bigg')
r1.connect()
print(r1.get_show_output('show version'))