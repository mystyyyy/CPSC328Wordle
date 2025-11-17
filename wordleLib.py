# wordleLib.py
# Spencer Silva
# Computer Science Major
# Created 11/14/25
# Due 11/24/25
# CPSC328, Professor Walther
# Library functions for Wordle application

import sys
import socket


# getWord retrieves the word from a socket, and ensures it is 5 characters or less.
# This both ensures that the word is within the valid range and helps to sanitize 
# the input.  Returns the string unless it is greater than 5, else returns 0.
def getWord(socket sock):
    input = sock.recv(1024).decode('utf-8')
    if len(input) <= 5:
        return input
    else:
        return 0


# strComp compares the user input word to the word chosen by the game, returning
# a 5-tuple on the status of the letters used. 0 means it is not present at all, 
# 1 means it is in the word, but in the wrong location, and 2 means it is in the 
# correct location.

def strComp(userIn, word):
    returnTuple = (0, 0, 0, 0, 0)
    counter = 0
    for letter in userIn:
        for compLetter in word:
            if letter == compLetter:
                returnTuple[counter] = 1
        if letter == word[counter]:
            returnTuple[counter] = 2
        counter++
    return returnTuple
    

