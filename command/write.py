# !/usr/bin/python

from generic_command import *


class Write(GenericCommand):
    @property
    def _get_value(self):
        val = re.split(',', self._command)[1]
        val = '0' * (2 * int(self._command[-1:]) - len(val)) + val
        return val

    @property
    def _generate_result(self):
        self._wait_result = True
        self._command = self._type + self._get_addr + ',' + self._command[-1:] + ':' + self._get_value
        return "$" + self._command + '#' + self._get_checksum

    def _print_result(self, target):
        res_ = target.recv_value(1024)
        while res_[:2] == "T0":
            res_ = target.recv_value(1024)
        print res_
