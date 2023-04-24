import socket
import select

# Define some constants
HOST = ''  # Bind to all available interfaces
PORT = 5000
MAX_CLIENTS = 10
BUFFER_SIZE = 1024

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(MAX_CLIENTS)
print(f"Server started on port {PORT}")

# Set up the list of sockets to monitor for incoming data
sockets_list = [server_socket]

# Set up a dictionary to store client usernames
client_usernames = {}

def handle_new_client(client_socket):
    """
    Handles the initial handshake with a new client,
    requesting their desired username and sending a welcome message.
    """
    client_socket.send("Enter your desired username: ".encode())
    username = client_socket.recv(BUFFER_SIZE).decode().strip()
    client_usernames[client_socket] = username
    welcome_message = f"Welcome to the chat, {username}!\n"
    broadcast(welcome_message, server_socket)

    # Continuously receive messages from the client
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode().strip()
            if message:
                username = client_usernames[client_socket]
                full_message = f"{username}: {message}\n"
                broadcast(full_message, exclude_socket=client_socket)
            else:
                # Handle broken connections
                client_socket.close()
                sockets_list.remove(client_socket)
                if client_socket in client_usernames:
                    del client_usernames[client_socket]
                break
        except:
            # Handle broken connections
            client_socket.close()
            sockets_list.remove(client_socket)
            if client_socket in client_usernames:
                del client_usernames[client_socket]
            break


def broadcast(message, exclude_socket=None):
    """
    Sends a message to all connected clients except for the one
    specified in exclude_socket (if any).
    """
    for socket in sockets_list:
        if socket != server_socket and socket != exclude_socket:
            try:
                socket.send(message.encode())
            except:
                # Handle broken connections
                socket.close()
                sockets_list.remove(socket)
                if socket in client_usernames:
                    del client_usernames[socket]

while True:
    # Use select to wait for sockets to become readable
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for socket in read_sockets:
        if socket == server_socket:
            # Handle new client connections
            client_socket, client_address = server_socket.accept()
            print(f"New client connected from {client_address}")
            sockets_list.append(client_socket)
            handle_new_client(client_socket)
        else:
            # Handle incoming messages from clients
            message = socket.recv(BUFFER_SIZE).decode().strip()
            if message:
                username = client_usernames[socket]
                full_message = f"{username}: {message}\n"
                broadcast(full_message, exclude_socket=socket)
            else:
                # Handle broken connections
                socket.close()
                sockets_list.remove(socket)
                if socket in client_usernames:
                    del client_usernames[socket]
