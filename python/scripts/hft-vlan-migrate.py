import paramiko
import time
import base64

cvlan = raw_input('Enter Vlans to migrate in x,y format: ')

cchost = cal-dc1-agg-n77-gw

with open('cal-dc1-agg-n77-gw.db', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		if 'switchport' in line:
			command = line + cvlan
		else
			command = line
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		new_ssh.send(command)
new_ssh.close



cchost = cal-dc2-agg-n77-gw

with open('cal-dc2-agg-n77-gw.db', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		if 'switchport' in line:
			command = line + cvlan
		else
			command = line
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		new_ssh.send(command)
new_ssh.close



cchost = cal-dc1-acc-n9k-sw

with open('cal-dc1-acc-n9k-sw.db', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		if 'switchport' in line:
			command = line + cvlan
		else
			command = line
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		new_ssh.send(command)

new_ssh.close



cchost = cal-dc2-acc-n9k-sw

with open('cal-dc2-acc-n9k-sw.db', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		if 'switchport' in line:
			command = line + cvlan
		else
			command = line
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		new_ssh.send(command)

new_ssh.close



cchost = cal-dc1-acc-n6k-sw

with open('cal-dc1-acc-n6k-sw.db', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		if 'switchport' in line:
			command = line + cvlan
		else
			command = line
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		new_ssh.send(command)

new_ssh.close



cchost = cal-dc2-acc-n6k-sw
with open('cal-dc2-acc-n6k-sw.db', 'r') as command_read:
	for line in command_read:																											
		line = line.strip().lower()
		if 'switchport' in line:
			command = line + cvlan
		else
			command = line
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())																																
		ssh.connect(cchost, username='admin', password='cc2lake', look_for_keys=False, allow_agent=False)
		new_ssh = ssh.invoke_shell()
		new_ssh.send(command)

new_ssh.close
