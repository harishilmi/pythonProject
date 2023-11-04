#get config in xml using ncclien

from ncclient import manager

iosxe = {'host': 'iosxe',
         'port': 830,
         'username': 'admin',
         'password': 'bigg',
         'hostkey_verify': False,
         'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**iosxe)
output = rtr_mgr.get_config('running')
print(type(output))
output = rtr_mgr.get_config('running').data_xml
print(type(output))
print(output)
with open('conf.xml', 'w') as f:
    f.write(output)
rtr_mgr.close_session()
