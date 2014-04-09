#!/usr/bin/python

from command import *
from target import *

def get_command(command):
	if (command[0] == "m"):
		return read.Read(command)
	elif (command[0] == "w"):
		return write.Write(command)
	else:
		return None

input_command = ""
input_command = raw_input('Enter command to read or write: ')
target = tcp_target.Tcp_target("localhost", 1235)

while ('exit' != input_command ):
	input_command = "".join(input_command.split())
	command_obj = get_command(input_command)
	if (command_obj is None):
		input_command = raw_input('Enter command to read or write: ')
		continue
	command_obj.execute(target)
	input_command = raw_input('Enter command to read or write: ')
