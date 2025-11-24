 Authors:        Alex Lowe, Brandon H. Nguyen, Spencer Silva                                                       
 Creation Date:  November 14, 2025                               
 Due Date:       November 24, 2025                               
 Course:         Network and Secure Programming (CPSC328-020)    
 Professor Name: Professor Walther                               
 Assignment:     Team Assignment - Application                   
 Filename:       README.txt                          
 Purpose:        Create a Wordle application that allows many    
                 users to play simultaneously. Server will hold 
                 word bank. The client will perform the game    
                 processing and user interface.                


TEAM MEMBERS 
Alex Lowe - Client-Side of Wordle Application
Brandon Nguyen - Server-Side of Wordle Application and team leader
Spencer Silva - Library for Wordle Application


PROJECT DESCRIPTION
An implementation of the game Wordle, where the server provides a
word to the client and the client needs to guess what the word is, 
and each guess reveals information about the word.  If a letter
from the client's guess is in the correct location in the word,
it will be marked as green.  If the letter is in the word, but not
in the correct location, it will be marked as yellow.  Lastly, if
the letter is not in the word at all, it will be marked as grey.


COMPILING THE CLIENT AND SERVER
Compiling is not needed, since Python is an interpreted language


HOW TO RUN THE CLIENT
    python wordleClient.py <host> <port>
    Ensure that the library file is also present

Client-side example:
    python wordleClient.py 127.0.0.1 9999


HOW TO RUN THE SERVER
    python wordleServerBNGuyen.py
    Ensure that the library file is also present


LIBRARY TYPE
Should be a shared library due to the way Python handles things.


ABOUT THE WORDLE PROTOCOL
1. Client and server establish the TCP three-way handshake, establishing a proper TCP connection.
2. Server sends a word from its bank to the client
3. Client then initiates the game using the word it was given.
4. After the game concludes, the client can choose to play again, returning to step 2
   or can choose to quit
5. The client disconnects from the server, ending the connection and terminatinating the thread on
   the server side.


KNOWN ISSUES WITH THE APPLICATION




TEAM DYNAMIC
Brandon acted as the group leader.
