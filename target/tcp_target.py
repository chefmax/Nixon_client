# !/usr/bin/python

import socket


class TcpTarget(object):
    sock = socket.socket()

    target = None

    def __new__(cls, *dt):
        if cls.target is None:
            cls.target = object.__new__(cls, *dt)
        return cls.target

    def __init__(self, host, port):
        self._host = host
        self._port = port
        TcpTarget.sock.connect((host, port))
        TcpTarget.sock.send('$QStartNoAckMode#b0')
        TcpTarget.sock.recv(1024)
        TcpTarget.sock.recv(1024)
        TcpTarget.sock.send('$P#50')
        TcpTarget.sock.recv(1024)
        TcpTarget.sock.send('$c#63')

    def __del__(self):
        TcpTarget.sock.close

    @staticmethod
    def send(content):
        TcpTarget.sock.send(content)

    @staticmethod
    def ntohl(content):
        return socket.ntohl(content)

    @staticmethod
    def recv_value(number):
        return TcpTarget.sock.recv(number)[1:-3]

    @staticmethod
    def recv(number):
        return TcpTarget.sock.recv(number)
