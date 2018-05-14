import paramiko
import time
import base64

cchost = raw_input('Enter Device Name or IP Address: ')

commands = ['show mac address']

intf = 'gi'

with open('files/mac-address.txt', 'w') as f:																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																								
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
 	ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
 	time.sleep(1)
 	for command in commands:
		stdin, stdout, stderr = ssh.exec_command(command)
		mac_out = stdout.channel.recv(8000)
		f.write(mac_out)

	ssh.close()


with open('files/mac-address.txt', 'r') as mac_read:
	for line in mac_read:																											
		line = line.strip().lower()
		if intf in line:
			mac_table = line.split()
			with open('files/master-device-table.txt', 'r') as master_read:
				for line in master_read:
					line = line.strip().lower()
					if mac_table[1] in line:
						master_table = line.split(",")
						#print 'Interface ' + mac_table[3] + '   Description ' + master_table[1]
						commands = ['config t\n', 'int ' + mac_table[3] + '\n', 'Description ' + master_table[1] + '\n']
						ssh = paramiko.SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
 						ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
						new_ssh = ssh.invoke_shell()
						for command in commands:
							new_ssh.send(command)
						new_ssh.close()