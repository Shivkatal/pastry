# server.py 
import socket                                         
import time
from ClientThread import ClientThread
import random
from SocketServer import ThreadingMixIn

TCP_IP = "localhost"
TCP_PORT = 9000 + int(random.random()*1000)

def server():
	# create a socket object
	serversocket = socket.socket(
		        socket.AF_INET, socket.SOCK_STREAM) 
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# get local machine name
	host = TCP_IP                          

	port = TCP_PORT                                           

	# bind to the port
	serversocket.bind((host, port))                                  
	print "Server started at",str(port)
	# queue up to 5 requests
	threads = []                                         

	while True:
		serversocket.listen(5)
		clientsocket,addr = serversocket.accept()
		print "Got a connection from %s" % str(addr)
		newThread = ClientThread(host, port, clientsocket)
		newThread.start()
		threads.append(newThread)

	for t in threads:
		t.join()	    


def client():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# get local machine name
	host = TCP_IP                           

	port = int(raw_input())

	# connection to hostname on the port.
	s.connect((host, port))                               

	# Receive no more than 1024 bytes
	tm = s.recv(1024)                                     
	m = str(raw_input())
	s.send(m)
	s.close()
	print("The time got from the server is %s" % tm.decode('ascii'))

print "Enter your choice:"
print "1.Server\n2.Client"
choice = int(raw_input())
if choice == 1:
	server()
elif choice == 2:
	client()