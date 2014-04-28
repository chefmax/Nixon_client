# !/usr/bin/python

from generic_command import *


class Write(GenericCommand):
    @property
    def _get_value(self):
        val = re.split(',', self._command)[1]
        if 1 == len(val):
            val = '0' + val
        return val

    @property
    def _generate_result(self):
        self._command = self._type + self._get_addr + ',' + self._command[-1:] + ':' + self._get_value
        return "$" + self._command + '#' + self._get_checksum
