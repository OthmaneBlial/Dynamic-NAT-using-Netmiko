from netmiko import ConnectHandler
import data



def show_nat_trans(R):
		print(20*'*'+' Showing NAT translations for Router 1 ' + 20*'*')
		net_connect = ConnectHandler(**R)
		output = net_connect.send_command('show ip nat trans')
		print(output)