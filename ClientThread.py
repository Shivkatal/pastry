import socket
from threading import Thread
import random
import time
from SocketServer import ThreadingMixIn



class ClientThread(Thread):

	def __init__(self,ip,port,sock):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.sock = sock
		print "New thread started for "+ip+":"+str(port)

	def run(self):
		currentTime = time.ctime(time.time()) + "\r\n"
		self.sock.send(currentTime.encode('ascii'))
		m = self.sock.recv(100)
		print m
		self.sock.close()

