#get config in xml using ncclien

from ncclient import manager
import xml.dom.minidom as md

iosxe = {'host': 'iosxe',
         'port': 830,
         'username': 'admin',
         'password': 'bigg',
         'hostkey_verify': False,
         'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**iosxe)
output = rtr_mgr.get_config('running')
xmldata = md.parseString(str(output))
new_data = xmldata.toprettyxml(indent="  ")
print(new_data)
# print(type(output))
# output = rtr_mgr.get_config('running').data_xml
# print(type(output))
# print(output)
with open('conf_pretty.xml', 'w') as f:
    f.write(new_data)
rtr_mgr.close_session()
