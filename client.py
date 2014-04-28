# !/usr/bin/python

from command import *
from target import *


def get_command(command):
    if "m" == command[0]:
        return read.Read(command)
    elif command[0] == "w":
        return write.Write(command)
    elif (command[0] == 'Z') or (command[0] == 'z'):
        return breakpoint.Breakpoint(command)
    else:
        return None


input_command = ""
input_command = raw_input('Enter command to read or write: ')
target = tcp_target.TcpTarget("localhost", 1235)

while input_command != 'exit':
    input_command = "".join(input_command.split())
    command_obj = get_command(input_command)
    if command_obj is None:
        input_command = raw_input('Enter command to read or write: ')
        continue

    command_obj.execute(target)
    input_command = raw_input('Enter command to read or write: ')
