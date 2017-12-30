import socket
import os
from sys import *
	
def pkt_sniffer(i):
    sniffer=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    sniffer.bind(('0.0.0.0',0))
    sniffer.setsockopt(socket.SOL_IP,socket.IP_HDRINCL,1)
    print ('packet number :'+str(i))
    print ('---------------------------------------------------------\n')
    print (sniffer.recvfrom(65565))
i=1
if platform == 'win32':
    os.system('cls')
else:
    os.system('clear')
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print ('$                                                                 $')
print ('$        The Packet sniffer welcomes you!!!!                      $')
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print ("Sniffer is successfully activated!! ")
print ("Please press q to exit sniffing:")			
while True:
    pkt_sniffer(i)
    i=i+1

