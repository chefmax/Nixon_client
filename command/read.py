# !/usr/bin/python

from generic_command import *


class Read(GenericCommand):
    @property
    def _generate_result(self):
        self._command = self._type + self._get_addr + self._command[-2:]
        return "$" + self._command + '#' + self._get_checksum

    def _print_result(self, target):
        print hex(target.recv_value(1024))
