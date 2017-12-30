# Python program to implement client side of chat room.
import socket
import select
import sys
import os
from sys import platform
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print "Correct usage: script, IP address, port number"
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

	# maintains a list of possible input streams
	sockets_list = [sys.stdin, server]

	""" There are two possible input situations. Either the
	user wants to give manual input to send to other people,
	or the server is sending a message to be printed on the
	screen. Select returns from sockets_list, the stream that
	is reader for input. So for example, if the server wants
	to send a message, then the if condition will hold true
	below.If the user wants to send a message, the else
	condition will f as true"""
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
                        if platform =="win32":
                            os.system('cls')
                        else:
                            os.system('clear')
                        print "####################################################################"
                        print "#------------------------------------------------------------------#"
                        print "#----------------The Mo&t $ecure Ch@tting Application!!------------#"
                        print "####################################################################"
                        name=raw_input("Please enter your name Dude >> :")
			print message
                        print "Hello "+name +" you are online now:"
                        print "Enjoy!!!"
                        print "*********************************************************************"
                        print "*                                                                   *"
                        print "*           The Chat Platform Is Now Ready For You!!                *"
                        print "*********************************************************************"
		else:
			message = sys.stdin.readline()
			server.send(name)
                        server.send(message)
			sys.stdout.write("|"+name+"-->"+message)
			#sys.stdout.write(message)
			sys.stdout.flush()
#name=raw_input("Please enter your name dude:")
server.close()
