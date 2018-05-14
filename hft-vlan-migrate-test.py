import paramiko
import time
import base64
import string

cvlan = raw_input('Enter Vlans to migrate in x,y format: ')

with open('/home/sssuser/HFT/roles/cal-dc1-agg-n7k-gw/files/vlan.cfg', 'w') as f:
	with open('cal-dc1-n7k-gw.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			#command = line.replace("X4Y7D","23")
			f.write(comm)
			f.write('\n')
	
		


