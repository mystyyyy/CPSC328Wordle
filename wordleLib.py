###################################################################
# Author:         Spencer Silva                                   #
# Major:          Computer Science                                #
# Creation Date:  November 14, 2025                               #
# Due Date:       November 24, 2025                               #
# Course:         Network and Secure Programming (CPSC328-020)    #
# Professor Name: Professor Walther                               #
# Assignment:     Team Assignment - Application                   #
# Filename:       wordleLib.py                                    #
# Purpose:        Create a Wordle application that allows many    #
#                 users to play simultaneously. Library           #
#                 contains functions used between both the        #
#                 client and server.                              #
###################################################################


import sys
import socket


# Function Name: sendWord
# Description:   Sends a user input message to the socket to be received by getWord
#                This contains error checking to ensure the entered message isn't 
#                longer than the max number of characters of 5
# Parameters:    sock- The socket to be used for data transfer
# Returns:       N/A
def sendWord(sock):
    text = input()
    if isinstance(text, str):
        if len(text) <= 5:  # check length
            sock.send(text.encode())
            return
    print("Error: Input is invalid, ensure input is 5 characters or less\n")
    return


# Function Name: sendMessage
# Description:   Sends a predefined message to the socket to be received by getWord
#                This contains error checking to ensure the entered message isn't 
#                longer than the max number of characters of 5
# Parameters:    sock- The socket to be used for data transfer
#                text- The string to be sent through the socket
# Returns:       N/A
def sendMessage(sock, text):
    if isinstance(text, str):
        if len(text) <= 5:
            sock.send(text.encode())
            return
    print("Error: Message being sent by system is invalid")
    return
    

# Function Name: getWordFrom
# Description:   Retrieves the word from a socket, and ensures it is 5 characters or less.
#                This both ensures that the word is within the valid range and helps to sanitize 
#                the input.
# Parameters:    sock- The socket to be used for data transfer
# Return Value:  Returns the uppercase string unless it is more than 5 characters long, else returns 0.
def getWordFrom(sock):
    input = sock.recv(1024).decode('utf-8')
    if isinstance(input, str):
        if len(input) <= 5:
            return input.upper()
    return 0


# strComp compares the user input word to the word chosen by the game, returning
# a 5-tuple on the status of the letters used. 0 means it is not present at all, 
# 1 means it is in the word, but in the wrong location, and 2 means it is in the 
# correct location.

# Unused and unfinished, only used client-side, so is not needed in library.

#def strComp(userIn, word):
#    returnTuple = (0, 0, 0, 0, 0)
#    counter = 0
#    
#    # compare each letter to the word
#    for letter in userIn.upper():
#        for compLetter in word.upper():
#            if letter == compLetter:
#                returnTuple[counter] = 1
#       if letter == word[counter]:
#            returnTuple[counter] = 2
#        counter = counter + 1
    
#    return returnTuple


# Function Name: socketCreation
# Description:   Creates a socket. If an exception is raised, print
#                out an error.
# Parameters:    N/A
# Return Value:  sock - Newly created socket object
def socketCreation():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError as e:
        print("Socket creation went wrong/failed.")
        print("Error: ", e)
        sys.exit()
    return sock


# Function Name: socketValidation
# Description:   Checks if the port is a valid port number
# Parameters:    port- an integer to be used for the port number
# Return Value:  True if valid, False if invalid
def socketValidation(port):
    if port < 0 or port > 65535:
        print("Invalid port number")
        return False
    if not isinstance(port, int):
        return False
    return True