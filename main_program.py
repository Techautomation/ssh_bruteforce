import argparse
from sys import platform
import os
import time
import socket
if platform=='win32':
    os.system('cls')
else:
    os.system('clear')

print '----------------------------------------------------------------------'
print '@                                                                    @'
print '@            Welcome to the program launcher!!                       @'
print '----------------------------------------------------------------------'

print '             This includes five programs:                             '
parser=argparse.ArgumentParser(description='Just run the main_program.py without any argument ,and select any option from the list to perform:')
args = parser.parse_args()
print "A) Ssh_Bruteforce\n\
B) Reverse_Shell \n\
C) Packet_Sniffer\n\
D) Chat_Server\n\
E) Open_Any_Locked_Zip_File_With_Dictionary\n"
while True: 
    choice= raw_input("Please select the desired program [ex:a,b,c,d,e]:and q to quit:->").upper()
    if choice=="A":
        hostname=raw_input("Enter the hostname of the ssh server:")
        username=raw_input("Enter the username for login:")
        os.system('python Ssh_Bruteforce.py -H hostname -u username -F password.txt')
        time.sleep(5)
    elif choice=="B":
        os.system('python3 Reverse_Shell_Server.py')
    elif choice=="C":
        os.system('python Packet_Sniffer.py')
    elif choice=="D":
        ip=socket.gethostbyname(socket.gethostname())
        os.system('python Chat_Server.py')
    elif choice=="E":
        file=raw_input('Enter the name of the locked zip file:>')
        dictionary=raw_input('Enter the dictionary file name :>')
        os.system('python Open_Locked_Zip.py -f file -d dictionary')
    elif choice=="Q":
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        print "@                       Thank-You!! For Using This Tool.                    @"
        print "@  Feel Free To Edit The Code, To Make It More Accurate And User Freindly.  @"
        print "@                             Bye-Bye!!!                                    @"
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        time.sleep(5)
        exit()
    else:
        print"Please Enter the valid option"
