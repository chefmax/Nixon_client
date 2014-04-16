#!/usr/bin/python

import socket

class Tcp_target(object):

	sock = socket.socket()

	target = None

	def __new__(cls, *dt, **mp):
		if cls.target is None:
			cls.target = object.__new__(cls, *dt, **mp)
		return cls.target

	def __init__(self, host, port):
		self._host = host
		self._port = port
		Tcp_target.sock.connect((host, port))
		Tcp_target.sock.send('$QStartNoAckMode#b0')
		Tcp_target.sock.recv(1024)
		Tcp_target.sock.recv(1024)

	def __del__(self):
		Tcp_target.sock.close

	def send(self, content):
		Tcp_target.sock.send(content)

	@classmethod
	def ntohl(cls, content):
		return socket.ntohl(content)

	def recv_value(self, number):
		return Tcp_target.ntohl(int(Tcp_target.sock.recv(number)[1:-3], 16))

	def recv(self, number):
		return Tcp_target.sock.recv(number)
