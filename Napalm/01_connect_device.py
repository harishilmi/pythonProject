from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'bigg' } #enable password
ios = driver('router1', 'bigg', 'bigg', optional_args=optional_args)
ios.open()


output = ios.get_bgp_neighbors()
print(output)
# print(dir(ios))


ios.close()