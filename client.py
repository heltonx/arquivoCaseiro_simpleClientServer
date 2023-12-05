import socket
client_socket = socket.socket()
server_address = 'localhost'
server_port = 455
client_socket.connect((server_address, server_port))
print client_socket.recv(1024)
 
client_socket.close()
