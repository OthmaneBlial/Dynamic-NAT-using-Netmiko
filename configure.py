from netmiko import ConnectHandler
import data

masks_table = {'1':'128', '2': '192', '3': '224', '4': '240', '5':'248', '6':'252', '7':'254', '8': '255'}

def convert_mask(mask):
	if (int(mask) <= 8):
		res = (masks_table[str(mask)]) + '.0.0.0'
	if (8 < int(mask) <= 16):
		res = '255.' + (masks_table[str(int(mask) - 8)]) + '.0.0'
	if (16 < int(mask) <= 24):
		res = '255.255.' + (masks_table[str(int(mask) - 16)]) + '.0'
	if (24 < int(mask) <= 32):
		res = '255.255.255.' + (masks_table[str(int(mask) - 24)])

	return res

def wild_card_of_mask(mask):
	converted_mask_list = convert_mask(mask).split('.')
	wild_card_list = []
	for el in converted_mask_list:
		wild_card_list.append(str(255 - int(el)))

	return '.'.join(wild_card_list)


def config_interface(interface, address, mask):
	return ['int '+ interface, 'ip add '+ address + ' ' + convert_mask(mask), 'no sh']

def config_default_route(dst):
	return ['ip route 0.0.0.0 0.0.0.0 ' + dst]

def config_interface_nat(interface, mode):
	return ['int '+ interface, 'ip nat '+ mode]

def config_acl(acl_id, method, network, mask):
	return ['access-list '+ acl_id + ' ' + method + network + ' ' + wild_card_of_mask(mask)]

def config_nat(pool_name, pool_start, pool_end, pool_prefix_length, acl_id):
	return ['ip nat pool '+ pool_name + ' ' + pool_start + ' ' + pool_end + ' prefix_length ' + pool_prefix_length,
	 'ip nat inside source list '+ acl_id + ' pool ' + pool_name]




def configure_R1(R1):
	print('Applying configuration to ROUTER 1')
	net_connect = ConnectHandler(**R1)
	config_commands = config_interface('f0/0', '10.10.10.1', '24') + config_interface('f1/0', '77.77.77.1', '24')
	config_commands += config_default_route('77.77.77.2')
	config_commands += config_interface_nat('f0/0', 'inside') + config_interface_nat('f1/0', 'outside')
	config_commands += config_acl('1', 'permit', '10.10.10.0', '24')
	config_commands += config_nat('the_pool', '77.77.77.50', '77.77.77.80', '25', '1')
	net_connect.send_config_set(config_commands)
	print("Configuration has been applied!")

def configure_R2(R2):
	print('Applying configuration to ROUTER 2')
	net_connect = ConnectHandler(**R2)
	config_commands = config_interface('f1/0', '77.77.77.2', '24')
	config_commands += config_interface('loop 0', '22.22.22.22', '24')
	net_connect.send_config_set(config_commands)
	print("Configuration has been applied!")

R1 = data.R1
R2 = data.R2

configure_R1(R1)
configure_R2(R2)
