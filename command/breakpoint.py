# !/usr/bin/python

from generic_command import *


class Breakpoint(GenericCommand):
    __breakpoints__ = {}

    @staticmethod
    def _maybe_insert_or_remove_breakpoint(command, addr):
        if command == 'Z':
            if addr in Breakpoint.__breakpoints__:
                return False, "Breakpoint on this address already exists!"
            Breakpoint.__breakpoints__[addr] = 1
            return True, "Breakpoint added successfully!"
        else:
            if addr not in Breakpoint.__breakpoints__:
                return False, "Could not delete nonexistent breakpoint!"
            Breakpoint.__breakpoints__.pop(addr)
            return True, "Breakpoint removed successfully!"

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
        return '1'

    @property
    def _generate_result(self):
        self._wait_result = True
        res_ = Breakpoint._maybe_insert_or_remove_breakpoint(self._command[0], self._get_addr)
        if not res_[0]:
            return None, res_[1]
        self._command = self._type + self._get_breakpoint_type + ',' + self._get_addr + ',' + self._get_length
        return "$" + self._command + '#' + self._get_checksum, res_[1]

    def execute(self, target):
        res_ = self._generate_result
        print(res_[1])
        if res_[0]:
            target.send("$g#67")
            target.recv(1024)
            target.send(res_[0])
            self._print_result(target)

    def _print_result(self, target):
        res_ = target.recv_value(1024)
        while res_[:2] != "OK":
            res_ = target.recv_value(1024)
        print res_