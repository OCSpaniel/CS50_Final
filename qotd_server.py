#!/usr/bin/env python

import socket
import sys 
import random
from _thread import *
import time

#open quote file and load into list for printing
temp_file = open('quotes.txt','r',encoding='utf-8')
quotes = temp_file.readlines()

def threaded_client(connection):
    random.seed() #initiate random seed
    rand_num = random.randint(0,len(quotes)) #Ensures rand # inside list
    sent_quote = quotes[rand_num]
    while True: #Get Random quote from quote file
        print('',sent_quote)
        connection.sendall(sent_quote.encode('utf-8'))
        break
    connection.close()

def main():

    #Check for arguments with port number being second
    if(len(sys.argv) >= 2):
        #Set port number to argument 2
        port_number = sys.argv[1]
    else:
        port_number = input("Please enter an unused port number (traditonally 17 per RFC 865) \n");
    
    #Gather server host name and ip address, print them out
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ('Host Name = {}'.format(host_name))
    print ('IP Address = {}'.format(ip_address))
    
    #attempt to create socket and bind, print error message 
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", str(msg[1]))
        sys.exit(1)

    s.bind((ip_address, int(port_number)))
    s.listen(5) 
    print('Listening for connections.....')
    #On accept hand off to Client to allow multiple connections at the same time
    
    while True:
        
        connection, address = s.accept()
        print("Connected to client", address)
        start_new_thread(threaded_client,(connection,))
      
if __name__ == "__main__":
    main()