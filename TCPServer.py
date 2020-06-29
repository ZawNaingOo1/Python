"""
Messenger program using TCP socket 
Save as TCPServer.py
"""
import socket
def server_program():
    # get the hostname
    host = socket.gethostname() #locat host name
    port = 5000                 # port nunber above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance of server socket 
    #The bind() function takes tuple as argument
    server_socket.bind(("", port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("User " + str(address) + "says "+ str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection



server_program()
