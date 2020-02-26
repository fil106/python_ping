from datetime import datetime
from pythonping import ping
from threading import Thread
import ipaddress
import socket

def pingIp(ip, cnt):
	response_list = ping(ip, count=cnt)
	if response_list.success():
		print(ip)

def pingSubnet(subnet):
	"""Return the list of alive hosts in recieved subnet.

	Keyword arguments:
	subnet -- class instance from ipaddress.ip_network

	"""
	# subnet_cnt = subnet.num_addresses
	alive_list = []
	for ip in subnet:
		if ip != subnet[0] and ip != subnet.broadcast_address:
			t = Thread(target=pingIp, args=(str(ip), 2))
			t.start()
			print(t.name)
	return True

def isOpen(ip, port):
	"""Return True/False if port on host is available

	Keyword arguments:
	ip --- 
	port --- 

	"""
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		r = s.connect_ex((ip, port))
		if r == 0:
			result = True
		else:
			result = False
		s.close()
		return result

	except KeyboardInterrupt:
		print('You pressed Ctrl+C')
		sys.exit()

	except socket.gaierror:
		print('Hostname could not be resolved. Exiting')
		sys.exit()

	except socket.error:
		print("Couldn't connect to server")
		sys.exit()

check_port = 161
alive_list = pingSubnet(ipaddress.ip_network(input('Какую сеть пингуем?:')))

# for ip in alive_list:
# 	if isOpen(ip, check_port):
# 		print('{}:{} 	Open'.format(ip, check_port))