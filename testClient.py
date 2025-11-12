#for testing purposes. Test on 

import sys
import socket
import ipaddress

def main():
    host = "127.0.0.1"
    port = 9999

    sockaddr_in = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError:
        print("Socket creation went wrong.")
        return -1

    try:
        s.connect(sockaddr_in)
    except OSError:
        print("Socket connection went wrong.")
        return -1

    try:
        data = s.recv(512)
        print(data.decode())
    except OSError:
        print("Receiving data operation went wrong.")
        return -1

    s.close()

    return 0

main()