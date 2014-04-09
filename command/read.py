#!/usr/bin/python

from generic_command import *
import socket

class Read(Generic_command):
	def __init__(self, command):
		self._type = "$m"
		super(Read, self).__init__(command)

	def _print_result(self, s):
		print int(s.recv(1024)[1:-3], 16) #>> ((4 - int(self._command[-1])) << 3)
