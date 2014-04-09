#!/usr/bin/python

import socket
from command import *
from target import *

target = tcp_target.Tcp_target("localhost", 1235)

#s = socket.socket()
#host = "localhost"
#port = 1235
#s.connect((host, port))
#s.send('$QStartNoAckMode#b0')
#print s.recv(1024)
#print s.recv(1024)



def get_command(command):
	if (command[0] == "m"):
		return read.Read(command)
	elif (command[0] == "w"):
		return write.Write(command)
	else:
		return None

input_command = ""
input_command = raw_input('Enter command to read or write: ')


while ('exit' != input_command ):
	input_command = "".join(input_command.split())
	command_obj = get_command(input_command)
	if (command_obj == None):
		input_command = raw_input('Enter command to read or write: ')
		continue
#	print command_obj.generate_result()
	command_obj.execute(target)
#	s.send(command_obj.generate_result())
#	command_obj.print_result(s)
#	print socket.ntohl(int(s.recv(1024)[1:-3], 16)) >> ((4 - int(input_command[-1])) << 3)
	input_command = raw_input('Enter command to read or write: ')
#s.close
