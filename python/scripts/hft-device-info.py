import paramiko
import time
import base64

#host = raw_input('Enter Device Name: ')
host = 'cal-dc1-agg-n7k-gw'

#commands = ['config t\n', 'interface e2/3\n', 'switchport trunk allowed vlan add 23\n']

com = {}
cnt = 0
cvlan = '23'

with open('test.txt', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		print line
		commands = line
		#if 'switchport' in line:
		#	com[int(cnt)] = [ line + ' ' + cvlan ]
		#	cnt = cnt + 1
		#	print line
		#else:
		#	com[int(cnt)] = [ line ]
		#	print line
		#	cnt = cnt + 1

#commands = [com[0], com[1], com[2], com[3]]
#commands = com.values()

max_buffer = 65535

def clear_buffer(ssh):
	if ssh.recv_ready():
		return ssh.recv(max_buffer)
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
ssh.connect(host, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
new_ssh = ssh.invoke_shell()
output = clear_buffer(new_ssh)
time.sleep(1)
new_ssh.send("terminal length 0\n")
output = clear_buffer(new_ssh)
for command in commands:
	new_ssh.send(command)
	time.sleep(1)
	#output = new_ssh.recv(max_buffer)
	#print(output)
	#f.write(output)
new_ssh.close()

