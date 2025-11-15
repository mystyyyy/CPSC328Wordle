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
# https://realpython.com/python-sockets/
# https://stackoverflow.com/questions/12454675/whats-the-return-value-of-socket-accept-in-python
#
#
#
###################################################################


import sys
import socket
import ipaddress
import random

DEFAULTPORTNUM = 9999
# It can be assumed that the default IP address wil be local host!
HOST = "127.0.0.1"
# Theme: Food!
# Note: This is the only place I used AI(ChatGPT). Also tweaked list cause it kept putting in 6-letter words in the list :(
WORDLELIST = [
    "APPLE", "BACON", "BAGEL", "BEETS", "BERRY", "BREAD", "BROTH", "CANDY", "CAROB", "CHARD",
    "CHILI", "CHIVE", "COCOA", "CREAM", "CREPE", "CRISP", "CRUST", "CURRY", "DONUT", "DOUGH",
    "FEAST", "FLOUR", "FRIED", "FUDGE", "GRAPE", "GRAVY", "GUAVA", "HONEY", "HERBS", "ICING",
    "JELLY", "JUICE", "LEMON", "MANGO", "MEATY", "MINTY", "MOCHI", "ONION", "OLIVE", "PASTA",
    "PEACH", "PEARL", "PECAN", "PILAF", "PIZZA", "PLUMS", "PRUNE", "RAMEN", "SALAD", "SALSA", 
    "SAUCE", "SAUTE", "SEEDS", "SLICE", "SNACK", "SPICE", "SPICY", "STEAK", "STEWS", "SUGAR",
    "SWEET", "SYRUP", "TACOS", "TANGY", "TARTS", "TOAST", "TROUT", "TUNAS", "VEGAN", "WHEAT",
    "YEAST", "ZESTY", "CIDER", "BASIL", "BEANY", "BRINE", "CHOPS", "CRABS", "ROAST", "TREAT",
    "GRAIN", "CAPER", "DATES", "LEEKS", "CLOVE", "HOPPY", "DINER", "SPUDS", "BEANS", "LATTE",
    "SCONE", "CREMA", "MINTS", "THYME", "SUSHI", "CUMIN", "BOBBY"
]

# Function Name: main
# Description:   
#
#
# Parameters:    n/a
# Return Value:  0 - success
def main():
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except:
            print("Invalid port number")
            return -1

        if port < 0 or port > 65535:
            print("Invalid port number")
            return -1

        print("Wordle Application Server is running on port number:", port, "\n")
    else:
        port = DEFAULTPORTNUM
        print("Wordle Application Server is running on DEFAULT PORT NUMBER:", DEFAULTPORTNUM, "\n")


    socketCreation(HOST, port)

    #s.close()
    return 0

# Function Name: socketCreation
# Description:   Creates a socket, binds it, listen for connections, and
#                accepts any connection w/ error handling. Additionally
#                handles binding the socket if port number is already in use.
#                Once the connection is accepted, the server and client
#                will read/write eachother information.
# Parameters:    HOST - The IP address of the server
#                port - The port that the server will try to connect to
# Return Value:  n/a
def socketCreation(HOST, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError as e:
        print("Socket creation went wrong/failed.")
        print("Error: ", e)
        return -1

    # The loop is checking if the port number is already in use or not.
    # If the socket fails to bind, then an exception is raised, port num
    # Is incremented, and try again until it works.
    while True:
        try:
            sockaddr_in = (HOST, port)
            s.bind(sockaddr_in)
            break
        except OSError as e:
            print("Binding socket went wrong/failed.")
            print("Error: ", e)
            port = port + 1
            print("Trying again. Connecting to port number:", port)

    try:
        s.listen()
        print("TCP: Listening on port", sockaddr_in[1])
    except OSError as e:
        # check if the port is taken
        print("Socket listening went wrong/failed")
        print("Error: ", e)
        return -1

    # accept() returns the pair, (conn, address)
    # conn - new socket object that can be used to send/recv info
    # address - ip address bound to socket on client side
        # Note: Address is also a pair of the client IP addr + port number
        # Source: https://docs.python.org/3/library/socket.html#module-socket
    # when client connect, send "HELLO"
    try:
        conn, address = s.accept()
        data = "HELLO"
        conn.send(data.encode())
    except OSError as e:
        print("Server socket failed to accept incoming connection")
        print("Error: ", e)
        return -1

    print("TCP Connection:", address[0])
    # if server receives "READY" or "WORD": Send random word

    # if server receive "BYE" or "QUIT": client disconnects

main()