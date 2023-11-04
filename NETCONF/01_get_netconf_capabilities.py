# from ncclient import manager
#
# iosxe = {'host': 'iosxe',
#          'port': 830,
#          'username': 'admin',
#          'password': 'bigg',
#          'hostkey_verify': False,
#          'device_params': {'name': 'csr'}}
#
# rtr_manager = manager.connect(**iosxe)
# print(rtr_manager.server_capabilities)
# for capabilities in rtr_manager.server_capabilities:
#     print(capabilities)
#
# print(rtr_manager.connected)
# rtr_manager.close_session()
# print(rtr_manager.connected)

#################################

from ncclient import manager

iosxe = {'host': 'iosxe',
         'port': 830,
         'username': 'admin',
         'password': 'bigg',
         'hostkey_verify': False,
         'device_params': {'name': 'csr'}}

rtr_manager = manager.connect(**iosxe)
schema = rtr_manager.get_schema("ietf-interfaces")
print(schema)