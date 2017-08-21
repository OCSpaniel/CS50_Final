#!/usr/bin/env python

import socket
import sys
import time

def main():
    print("Welcome to the Quote of the day")
    print("Use ./qotd <port_number> <server address> to specify different port")
    if(len(sys.argv) >= 2):
        #Set port number to argument 2 and server address to user provided
        port_number = sys.argv[1]
        server_address = sys.argv[2]
    else: #Default to port 17 per RFC and localhost
        port_number = 17
        server_address = socket.gethostbyname(socket.gethostname())

    print("Attempting to establish connection to the server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, int(port_number)))
    b_quote = s.recv(1024)
    quote = b_quote.decode('utf-8')
    print('\n')
    print('', quote)
    print('\n')
    time.sleep(1)
    s.close()

if __name__ == "__main__":
    main()    


