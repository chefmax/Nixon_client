# !/usr/bin/python

from generic_command import *


class Breakpoint(GenericCommand):
    @property
    def _get_breakpoint_type(self):
        return self._command[1]

    @property
    def _get_addr(self):
        addr = re.split(',', self._command)[1]
        addr = "0" * (10 - len(addr)) + addr[2:]
        return addr

    @property
    def _get_length(self):
        return str(int(re.split(',', self._command)[2], 16))

    @property
    def _generate_result(self):
        self._wait_result = True
        self._command = self._type + self._get_breakpoint_type + ',' + self._get_addr + ',' + self._get_length
        return "$" + self._command + '#' + self._get_checksum

    def execute(self, target):
        target.send("$g#67")
        target.recv(1024)
        target.send(self._generate_result)
        self._print_result(target)