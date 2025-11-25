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
    python wordleServerBNGuyen.py [port]
    Ensure that the library file is also present
    The user can specify what port the server connects to
    If no port is given, then the default port, 9999, is used


LIBRARY TYPE
The library is a shared library because all files (client and server)
accesses the same file. Also because Python is an interpreted language,
and static libraries are created at compile time, it must be a shared
library.


ABOUT THE WORDLE PROTOCOL
1. Client and server establish the TCP three-way handshake, establishing a proper TCP connection.
    1a. Once established, the server sends "HELLO" to the client.
2. Server sends a word from its bank to the client
3. Client then is then prompted to say "WORD"/"READY," or "BYE"/"QUIT."
    3a. If the user says "WORD" or "READY," then the user initiates the game.
        The server sends a word from its bank to the client, and the user can start
        guessing the random word that was sent by the server.
    3b. If the user says "BYE" or "QUIT," then the server sends a message that the connection is
        terminated and the user disconnects from the server.
4. After the game concludes, the client can choose to play again or end the connection by answering 
    the prompt mentioned in part 3.

To synchronize the data, the client and server switches between sending and receiving data, and will
only proceed once it receives the information. Additionally there's a function in the wordle library
file where it matches the random word between the client and server so that the information remains
consistent.

KNOWN ISSUES WITH THE APPLICATION
N/A



TEAM DYNAMIC
Initially everyone worked together closely, then diverged to work on their respective part
of the project, and then lastly merged everything into the final project.

When someone had a question, everyone else assisted them until they understand/misunderstandings
are cleared up.

The team first created a basic connection between the client and server using sockets.

Brandon, who worked on the server consulted the network program assignment document to 
be in line with the requirements for the project. As the team leader he reviewed the other
team member's code to make sure the requirements for the project was being met.

Alex and Spencer worked on their respective part of the project to meet the requirements of 
the project.