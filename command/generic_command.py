# !/usr/bin/python
import re


class GenericCommand(object):
    obj = None

    def __new__(cls, *dt):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt)
        return cls.obj

    def __init__(self, command):
        self._type = command[0]
        self._command = command
        self._wait_result = False

    @property
    def _get_checksum(self):
        checksum = 0
        for i in range(0, len(self._command)):
            checksum += ord(self._command[i])
        checksum = (hex(checksum % 256))[2:]
        if 1 == len(checksum):
            checksum += '0'
        return checksum

    @property
    def _get_addr(self):
        addr = re.split(',', self._command)[0]
        addr = "0" * (11 - len(addr)) + addr[3:]
        return addr

    @property
    def _generate_result(self):
        return self._command

    def _print_result(self, target):
        if self._wait_result:
            print target.recv(1024)[1:-3]

    def execute(self, target):
        target.send(self._generate_result)
        self._print_result(target)
