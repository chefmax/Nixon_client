#!/usr/bin/python

from generic_command import *
import socket

class Read(Generic_command):

    @property
    def _generate_result(self):
        self._command = self._type + self._get_addr + self._command[-2:]
        return "$" + self._command + '#' + self._get_checksum

    def _print_result(self, target):
        print target.recv_value(1024) >> ((4 - int(self._command[-1])) << 3)
