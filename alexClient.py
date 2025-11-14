#####################################################################
# Author:          Alexander David Lowe                             #
# Major:           Computer Science                                 #
# Creation Date:   November 14th, 2025                              #
# Due Date:        November 24th, 2025                              #
# Course:          CPSC 328-020                                     #
# Professor Name:  Professor R. Walther                             #
# Assignment:      TEAM Project Application: Wordle                 #
# Filename:        wordleClient.py                                  #
# Purpose:         Client-side program that ...                     #
#                                                                   #
#                                                                   #
#                                                                   #
#####################################################################

import sys
import socket
import ipaddress

# host = "127.0.0.1"
# port = 9999

def main():
    (host, port) = set_port_and_host()
    make_connection(host, port)

    return 0



#####################################################################
# Function name:    set_port_and_host                               #
# Description:      Assigns port and host values based on command-  # 
#                   line argument input and returns them. Uses a    #
#                   default port number if one is not provided.     #
# Parameters:       N/A                                             # 
# Return Values:    host: the hostname of the client                # 
#                   port: the port number used by the server        #
#####################################################################
def set_port_and_host():

    if len(sys.argv) > 3:                                       # 3+ CLAs
        print("Error: Too many command-line arguments.\n")
        exit_usage()

    match len(sys.argv):                                        # How many CLAs are there?
        case 1:                                                 # 0 CLAs
            print("Error: Please provide a hostname.\n")
            exit_usage()
        case 2:                                                 # 1 CLA - Host specified only
            try:
                host = sys.argv[1]                              # User-specified host
                port = 9999
        case 3:                                                 # 2 CLAs - Host AND port num specified
            try: 
                host = sys.argv[1]                              # User-specified host
                port = int(sys.argv[2])                         # User-specified port number - check if int
            except ValueError:                                  # Error thrown by int()
                print("Error: Port Number must be an integer.\n")
                exit_usage()

    return host, port

#########################################################################
# Function name:   make_connection                                      #
# Description:     Uses host and port number to connect to the server   #
# Parameters:      hostname: name of the client running the application #
#                  portnum: port number of the server side application  #
# Return Value:    N/A                                                  #
#########################################################################
def make_connection(hostname, portnum):
    try:
        serverAddress = (hostname, portnum)                     # Specify server address
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create socket object
        s.connect(serverAddress)                                # Connect to server 
        print(f"Connected to {hostname}:{portnum}")
    except OSError:
        print(f"Error: Connection to {hostname}:{portnum} failed.")
        

#########################################################################
# Function name:   exit_usage                                           #
# Description:     Exits the program and prints the proper usage of     #   
#                  command-line arguments                               #
# Parameters:      none                                                 #
# Return Value:    int - the person’s age                               #
#########################################################################
def exit_usage():
    sys.exit("Usage:\n./a.out <Hostname>, <Port Number>\n")


main()