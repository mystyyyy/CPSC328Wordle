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
#
###################################################################


import sys
import socket
import ipaddress
import random

DEFAULTPORTNUM = 9999
HOST = "127.0.0.1"
# Theme: Food!
# Note: This is the only place I used AI. Also tweaked list cause it kept putting in 6-letter words in the list :(
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
    "SCONE", "CREMA", "MINTS", "THYME", "SUSHI", "CUMIN"
]

# Function Name: main
# Description:   
# Parameters:    
# Return Value:  
def main():
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        print("Wordle Application Server is running on port number:", port, "\n")
    else:
        #some default port num
        port = DEFAULTPORTNUM
        print("Wordle Application Server is running on DEFAULT PORT NUMBER:", DEFAULTPORTNUM, "\n")
        print("Usage: ", sys.argv[0], " [port number]\nPort Number - Specified port that server will run on.\n")
        #if port is in use:
        #    port = DEFAULTPORTNUM + 1

    sockaddr_in = (HOST, port)
    socketCreation(sockaddr_in)


    # Maybe? Close socket
    return 0

# Function Name: socketCreation
# Description:   
# Parameters:    
# Return Value:  
def socketCreation(sockaddr_in):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError:
        print("Socket creation went wrong/failed.")
        return -1
    
    try:
        s.bind(sockaddr_in)
    except OSError:
        print("Binding socket went wrong/failed.")
        return -1

    try:
        s.listen()
        print("TCP: Listening on port", sockaddr_in[1])
    except OSError as e:
        # check if the port is taken
        print("Socket listening went wrong/failed")
        return -1

    # accept() returns the pair, (conn, address)
    # conn - new socket object that can be used to send/recv info
    # address - ip address bound to socket on client side
    try:
        conn, address = s.accept()
        data = "HELLO"
        conn.send(data.encode())
    except OSError:
        print("Server socket failed to accept incoming connection")
        return -1

    print("TCP Connection from host:", address)
    # when client connect, send "HELLO"
    # if server receives "READY" or "WORD": Send random word
    # if server receive "BYE" or "QUIT": client disconnects


main()