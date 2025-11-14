#/*********************************************************************/
#/* Author:          Alexander David Lowe
#/* Major:           Computer Science  
#/* Creation Date:   November 14th, 2025
#/* Due Date:        November 24th, 2025
#/* Course:          CPSC 328-020  
#/* Professor Name:  Professor Walther
#/* Assignment:      TEAM Project Application: Wordle
#/* Filename:        wordleClient.py
#/* Purpose:         Client-side program that ...    
#/*                  
#/*                               
#/*                                
#/*********************************************************************/

import sys
import socket
import ipaddress

# host = "127.0.0.1"
# port = 9999

def main():

    return 0

# Takes CLAs if any given, uses default values otherwise
def set_port_and_host():
    match len(sys.argv):
        case 1: # No CLAs
            print("Error: Please provide a hostname.")
            exitUsage()
        case 2: # Host specified only
            try:
                host = sys.argv[1]
                port = 9999
        case 3: # Host AND port num specified
            try: 
                host = sys.argv[1]
                port = int(sys.argv[2])
            except ValueError:
                print("Error: Port Number must be an integer.")
                exitUsage()
    return host, port

# Connect to Server
def make_connection():
    serverAddress = (host, port)  # Specify server address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create socket object
    s.connect(serverAddress)    # 

# Exit program, print CLA usage
def exit_usage():
    sys.exit("Usage:\n./a.out <Hostname>, <Port Number>")


main()
