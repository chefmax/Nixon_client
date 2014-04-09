#!/usr/bin/python

from generic_command import *

class Write(Generic_command):
	def __init__(self, command):
		self._type = "$M"
		super(Write, self).__init__(command)

	def _get_value(self):
		val = re.split(',', self._command)[1]
		if (len(val) == 1):
			val = '0' + val
		print val
		return val

	def _generate_result(self):
		return self._type + self._get_addr() + ',' + self._command[-1:] + ':' + self._get_value()  + '#' + self._get_checksum()
