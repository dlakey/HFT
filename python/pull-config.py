import paramiko
import time
import base64
import sys
import cmd
import json
import yaml
import os

#host = raw_input('Enter Hostname or IP address of Device: ')
with open("cred.yaml", 'r') as stream:
	try:
		cred_data = yaml.load(stream)
		print(cred_data)
	except yaml.YAMLERROR as exc:
		print(exc)

#commands = ['show vlan']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(cred_data['host'], username=cred_data['username'], password=cred_data['password'], look_for_keys=False, allow_agent=False)
dev = ssh.invoke_shell()

# Enable Mode
#dev.send('enable\n')

#Enable Password
#dev.send('cc2lake\n')
resp = dev.recv(0)

#Turn of Terminal Paging
dev.send('terminal length 0\n')
resp = dev.recv(0)

#Dump Config
dev.send('show run\n')
time.sleep(3)
resp = dev.recv(49999)
counter = 0
print resp
with open('../roles/' + cred_data['host'] + '/files/' + cred_data['host'] + '.cfg', 'w') as f:
	for line in resp:
		f.write(line)


	#resp = dev.recv(9999)
	#print resp
