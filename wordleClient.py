#####################################################################
# Author:           Alexander David Lowe                            #
# Major:            Computer Science                                #
# Creation Date:    November 14th, 2025                             #
# Due Date:         November 24th, 2025                             #
# Course:           CPSC 328-020                                    #
# Professor Name:   Professor R. Walther                            #
# Assignment:       TEAM Project Application: Wordle                #
# Filename:         wordleClient.py                                 #
# Purpose:          Client-side application that connects to a      #
#                   server-side application using the TCP protocol  #
#                   to facilitate play of the game Wordle.          #
#                   Answer word is received from server.            #
#####################################################################

import sys
import string
import wordleLib

# host = "127.0.0.1"
# port = 9999

def main():
    # Setup 
    (host, port) = set_port_and_host()                      # Read CLAs
    sock = make_connection(host, port)                      # Connect to server
    handshake(sock)                                         # Verify connection
    print("Welcome to Wordle! You have 6 attempts to correctly guess the 5-letter answer word.")

    # Game Loop
    playing = True
    while playing == True:
        answer_word = wordleLib.getWordFrom(sock)               # Receiver answer word from server
        run_game(answer_word)
        playing = play_again(sock)

    # End Program
    end_connection(sock)
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

    elif len(sys.argv) == 1:                                    # 0 CLAs
        print("Error: Please provide a hostname.\n")
        exit_usage()

    elif len(sys.argv) == 2:                                    # 1 CLA (Host only)
        host = sys.argv[1]                                      # User-specified host
        port = 9999                                             # Default port number

    elif len(sys.argv) == 3:                                    # 2 CLAs (Host and Port)
        if wordleLib.socketValidation(sys.argv[2]) == False:    # Library function to validate port number
            exit_usage()
        try: 
            host = sys.argv[1]                                  # User-specified host
            port = int(sys.argv[2])                             # User-specified port number - check if int
        except ValueError:                                      # Error thrown by int() if non-int provided
            print("Error: Port Number must be an integer.\n")
            exit_usage()

    return host, port

#########################################################################
# Function name:    make_connection                                     #
# Description:      Uses host and port number to connect to the server  #
# Parameters:       hostname: name of the client running the            #
#                             application                               #
#                   portnum: port number of the server side application #
# Return Value:     s: the socket object created by function            #
#########################################################################
def make_connection(hostname, portnum):
    try:
        serverAddress = (hostname, portnum)                     # Specify server address
        s = wordleLib.socketCreation()                          # Library function to create socket w/ error checks
        s.connect(serverAddress)                                # Connect to server via socket
        print(f"Connected to {hostname} : {portnum}")
    except OSError:                                             # Error thrown by failure to connect
        print(f"Error: Connection to {hostname} : {portnum} failed.")
        exit_usage()
    
    return s
        
#########################################################################
# Function name:    handshake                                           #
# Description:      Verifies client-server connection with a three-way  #
#                   handshake.                                          #
# Parameters:       socket: the socket object created previously        #
# Return Value:     N/A                                                 #
#########################################################################
def handshake(socket):
    server_msg = socket.recv(1024).decode().strip()             # Receive message from server

    if server_msg != "HELLO":                                   # Check that message is "HELLO"
        print(f"Handshake Error: expected \"HELLO\" from server, but received {server_msg}\n")
        exit_usage()

    print(f"Server said: {server_msg}")                         # Print message from server
    wordleLib.sendMessage(socket, "READY")                      # Send "READY" to server

    return

#########################################################################
# Function name:    run_game                                            #
# Description:      Runs a loop that allows user to play wordle.        #
#                   Manages a series of lists that keep track of        #
#                   letters and how correct they are, updating with     #
#                   user-input guesses.                                 #
# Parameters:       answer: the answer word received from the server    #
# Return Value:     N/A                                                 #
#########################################################################
def run_game(answer):
    guesses_remaining = 6
    current_green_letters = []
    known_green_letters = ['_'] * 5
    yellow_letters = []
    gray_letters = []
    white_letters = list(string.ascii_uppercase)

    while guesses_remaining > 0:
        print(f"Guesses Remaining: {guesses_remaining}")
        guess = input().strip().upper()
        print(f"\nYou guessed: {guess}")

        # If guess contains non-letters, maker user try again
        if not guess.isalpha():
            print(f"Error: Guess must contain only letters.\n")
            continue

        # If guess does not contain exactly 5 letters, make user try again
        if not len(guess) == 5:
            print(f"Error: Guess must contain exactly 5 letters\n")
            continue

        # Reset list of current green letters for reassignment
        current_green_letters = ['_'] * 5

        # Sort guessed letters
        for i, char in enumerate(guess):                        # Iterare through letters in guess
            if char in white_letters:                           # Update unguessed (white) letters
                white_letters.remove(char)
            if char == answer[i]:
                known_green_letters[i] = char                   # Update known green letters
                current_green_letters[i] = char                 # Update current green letters
                if char in yellow_letters:
                    yellow_letters.remove(char)                 # Remove from yellow letters if now green
            elif char in answer and char not in yellow_letters and char not in known_green_letters:
                yellow_letters.append(char)                     # Update yellow letters
            elif char not in answer and char not in gray_letters:
                gray_letters.append(char)                       # Update wrong (gray) letters
            else:
                print(f"Error: Letter {char}")

        # Display guess info
        print(f"Green letters in this guess:\n{''.join(current_green_letters)}")
        print(f"All known green letters:\n{''.join(known_green_letters)}")
        print(f"All known yellow letters:\n{', '.join(yellow_letters)}")
        print(f"Unguessed letters:\n{', '.join(white_letters)}")
        print(f"Incorrect letters:\n{', '.join(gray_letters)}")
        
        # Decrement remaining guesses
        guesses_remaining -= 1

        # User wins
        if guess == answer:
            print(f"You guessed the word! Congratulations!")
            return

        # User loses
        if guesses_remaining == 0:
            print(f"You've run out of guesses! The word was:\n{answer}.\n")
            return

#########################################################################
# Function name:    play_again                                          #
# Description:      Asks user if they want to play again, returns true  #   
#                   True if yes (y), False if no (n)                    #
# Parameters:       socket: socket object used to communicate with      #
#                   server                                              #
# Return Value:     True or False                                       #
#########################################################################
def play_again(socket):
    print("Play again? (y/n)\n")
    while True:                                                 # Loop until valid response calls return
        response = input().strip().lower()
        if response == "y":
            print("\nStarting new game...\n")
            wordleLib.sendMessage(socket, "WORD")                      # Send "READY" to server
            return True
        elif response == "n":
            return False
        else:
            print("Invalid response. Please enter 'y' or 'n'.\n")

#########################################################################
# Function name:    exit_usage                                          #
# Description:      Exits the program and prints the proper usage of    #   
#                   command-line arguments                              #
# Parameters:       none                                                #
# Return Value:     none                                                #
#########################################################################
def exit_usage():
    sys.exit(f"Usage:\npython {sys.argv[0]} <Hostname>, <Port Number>\nOr, for default port number 9999:\npython {sys.argv[0]} <Hostname>")

#########################################################################
# Function name:    end_connection                                      #
# Description:      Sends BYE to server and closes socket connection,   #   
#                   prints goodbye message to user                      #
# Parameters:       sock: socket object used to communicate with server #
# Return Value:     none                                                #
#########################################################################
def end_connection(sock):
    wordleLib.sendMessage(sock, "BYE")                          # Send BYE to server
    sock.close()                                                # Close socket connection
    print("Thanks for playing!\n")                              # Print goodbye message                               

main()
