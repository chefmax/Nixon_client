# !/usr/bin/python

from generic_command import *


class Read(GenericCommand):
    @property
    def _generate_result(self):
        col = re.search(',', self._command)
        self._wait_result = True
        self._command = self._type + self._get_addr + ',' + re.split(',', self._command)[1]
        return "$" + self._command + '#' + self._get_checksum

    def _print_result(self, target):
        res_ = target.recv_value(1024)
        while res_[:2] == "T0":
            res_ = target.recv_value(1024)
        print res_
