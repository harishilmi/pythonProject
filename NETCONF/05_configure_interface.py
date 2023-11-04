from ncclient import manager

iosxe = {'host': 'iosxe',
         'port': 830,
         'username': 'admin',
         'password': 'bigg',
         'hostkey_verify': False,
         'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**iosxe)
#filter below will get the data for hostname and vrf available
interface_config = '''
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" >
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>2</name>
            <ip>
              <address>
                <primary>
                  <address>22.2.2.2</address>
                  <mask>255.255.255.0</mask>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
'''
output = rtr_mgr.edit_config(interface_config, target='running')
print(type(output))
print(output)

rtr_mgr.close_session()