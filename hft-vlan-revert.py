import time
import base64
import string

cvlan = raw_input('Enter Vlans to migrate in x,y format: ')

with open('/home/sssuser/HFT/roles/cal-dc1-agg-n7k-gw/files/vlan.cfg', 'w') as f:
	with open('cal-dc1-n7k-gw-back.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			f.write(comm)
			f.write('\n')
f.close()	
		

with open('/home/sssuser/HFT/roles/cal-dc2-agg-n7k-gw/files/vlan.cfg', 'w') as f:
	with open('cal-dc2-n7k-gw-back.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			f.write(comm)
			f.write('\n')
f.close()


with open('/home/sssuser/HFT/roles/cal-dc1-acc-n6k-sw/files/vlan.cfg', 'w') as f:
	with open('cal-dc1-n6k-sw-back.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			f.write(comm)
			f.write('\n')
f.close()	
		

with open('/home/sssuser/HFT/roles/cal-dc2-acc-n6k-sw/files/vlan.cfg', 'w') as f:
	with open('cal-dc2-n6k-sw-back.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			f.write(comm)
			f.write('\n')
f.close()


with open('/home/sssuser/HFT/roles/cal-dc1-acc-n9k-sw/files/vlan.cfg', 'w') as f:
	with open('cal-dc1-n9k-sw-back.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			f.write(comm)
			f.write('\n')
f.close()	
		

with open('/home/sssuser/HFT/roles/cal-dc2-acc-n9k-sw/files/vlan.cfg', 'w') as f:
	with open('cal-dc2-n9k-sw-back.txt', 'r') as command_read:
		for line in command_read:																											
			line = line.strip().lower()
			comm = string.replace(line, 'x4y7d', cvlan)
			f.write(comm)
			f.write('\n')
f.close()
