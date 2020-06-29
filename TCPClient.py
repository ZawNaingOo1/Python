"""
Messenger program using TCP socket
Save as TCPClient.py
"""

import socket

def client_program():
    host = "127.0.0.1"      #otherwise server ip address
    port = 5000             # socket server port number
    
    # instantiate client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))     # connect to the server

    #message = input(" -> ")                # input() gives error on client side, need raw_input
    try:
        input = raw_input
    except NameError:
        pass
    message = input("->")

    while message.lower().strip() != 'bye':         #stopping condition
        client_socket.send(message.encode())        # client send message to server
        data = client_socket.recv(1024).decode()    # receive response

        print('Received from server: ' + data)      # show in terminal

        message = input(" -> ")                     # again take input

    client_socket.close()                           # close the connection

client_program()
