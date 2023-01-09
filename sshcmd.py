import paramiko
import subprocess 

def ssh_cmd(user,ip,passwordd,cmdd,portt):
	command = cmdd
	
	# Update the next three lines with your
	# server's information
	
	host = ip
	username = user
	password = passwordd
	port=portt

	
	client = paramiko.client.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username=username, password=password,port=port)
	_stdin, _stdout,_stderr = client.exec_command(cmdd)
	#print(_stdout.read().decode())
	var=_stdout.read().decode()
	#print(var)
	client.close()
	return var
#ssh_cmd()

