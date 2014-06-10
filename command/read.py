# !/usr/bin/python

from generic_command import *


class Read(GenericCommand):
    @property
    def _generate_result(self):
        col = re.search(',',self._command)
        self._command = self._type + self._get_addr + ',' + re.split(',', self._command)[1]
        return "$" + self._command + '#' + self._get_checksum

    def _print_result(self, target):
        print target.recv_value(1024)
