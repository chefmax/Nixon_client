#!/usr/bin/python

from generic_command import *

class Breakpoint(Generic_command):

	def _get_breakpoint_type(self):
		return self._command[1]

	def _get_addr(self):
		addr = re.split(',',self._command)[1]
		addr = "0" * ( 10 - len(addr) ) + addr[2:]
		return addr

	def _get_length(self):
		return str(int(re.split(',',self._command)[2], 16))

	def _generate_result(self):
		self._command = self._type + self._get_breakpoint_type() + ',' + self._get_addr() + ',' + self._get_length()
		return "$" + self._command + '#' + self._get_checksum()
