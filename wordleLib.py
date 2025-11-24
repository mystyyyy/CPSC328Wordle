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



# sendWord sends a message to the socket to be received by getWord
# This contains error checking to ensure the entered message isn't longer than the
# max number of characters of 5
def sendWord(sock):
    text = input()
    if isinstance(input, str):
        if len(input) <= 5:
            sock.send(input.encode())
            return
    print("Input is invalid- Ensure input is 5 characters or less\n")
    return
    # maybe reprompt? maybe leave for client and server to decide
    
    


# getWordFrom retrieves the word from a socket, and ensures it is 5 characters or less.
# This both ensures that the word is within the valid range and helps to sanitize 
# the input.  Returns the string unless it is greater than 5, else returns 0.
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

def strComp(userIn, word):
    returnTuple = (0, 0, 0, 0, 0)
    counter = 0
    
    # compare each letter to the word
    for letter in userIn.upper():
        for compLetter in word.upper():
            if letter == compLetter:
                returnTuple[counter] = 1
        if letter == word[counter]:
            returnTuple[counter] = 2
        counter = counter + 1
        
    # now check for any duplicate letters in the submitted word
    # used to allow for the edge case of having the same letter be in the correct
    # location and incorrect location, and showing the player if there is another
    # instance of that letter in the current word
    
    return returnTuple