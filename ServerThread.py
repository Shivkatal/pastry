import socket
from threading import Thread
import random
import time
from SocketServer import ThreadingMixIn


class ServerThread(Thread):

	def __init__(self,func):
		Thread.__init__(self)
		self.func = func

	def run(self):
		self.func()

