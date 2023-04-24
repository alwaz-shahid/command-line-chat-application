import socket

HOST = ''
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server started on port {PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"New client connected from {client_address}")
    client_socket.close()
