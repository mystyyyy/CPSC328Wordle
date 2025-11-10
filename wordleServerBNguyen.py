###################################################################
# Author:         Brandon H Nguyen                                #
# Major:          Information Technology                          #
# Creation Date:  November 10, 2025                               #
# Due Date:       November 24, 2025                               #
# Course:         Network and Secure Programming (CPSC328-020)    #
# Professor Name: Professor Walther                               #
# Assignment:     Team Assignment - Application                   #
# Filename:       wordleServerBNguyen.py                          #
# Purpose:        Create a Wordle application that allows many    #
#                  users to play simultaneously. Server will hold #
#                  word bank. The client will perform the game    #
#                  processing and user interface.                 #
###################################################################
# SOURCES USED FOR PROJECT  :)                                    #
# https://docs.python.org/3/library/sys.html#module-sys           #
# https://docs.python.org/3/library/socket.html                   #
# https://docs.python.org/3/library/ipaddress.html                #
#
###################################################################


import sys
import socket
import ipaddress
# import signal?

# Theme: 
# Create a list of ~100-200 words

def main():
    # CLA
        # OPTIONAL - Connect to user specified port number
        # Else, connect to default port number
            #If port number is already in use, +1
    
    # Create socket
    # Bind socket to an address
    # Listen for connection
    # Accept connection

    # If server receive HELLO
    # If server receive WORD / READY
    # If server receive BYE / QUIT
    # One accepted information, send word

    # Maybe? Close socket
    return 0

main():