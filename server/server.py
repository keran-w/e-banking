import socket
import threading

def handle_client(client_socket, username):
    while True:
        # Receive data from client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        # Print message with username
        print(f'{username}: {data}')
        # Echo back to client
        client_socket.sendall(data.encode())
    # Close client socket
    client_socket.close()
    # Decrement client count and print disconnection message
    with client_count_lock:
        global client_count
        client_count -= 1
        print(f'{username} has disconnected. {client_count} clients remaining.')
        # Check if all clients have disconnected and close server socket if so
        if client_count == 0:
            server_socket.close()

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print('Server is listening on port 12345...')

# Initialize client count to 0 and a lock to synchronize access to it
client_count = 0
client_count_lock = threading.Lock()

# Handle incoming client connections
while True:
    client_socket, addr = server_socket.accept()
    # Prompt client for username
    username = client_socket.recv(1024).decode()
    print(f'{username} has connected from {addr}')
    # Increment client count and print total count
    with client_count_lock:
        client_count += 1
        print(f'{client_count} clients connected.')
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()
