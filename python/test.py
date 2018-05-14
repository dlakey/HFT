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
	