import socket

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Get username from user input
username = input('Enter a username: ')
# Send username to server
client_socket.sendall(username.encode())

while True:
    # Get user input
    message = input('Enter a message to send to the server: ')
    # Send message to server
    client_socket.sendall(message.encode())
    # Receive echo back from server
    data = client_socket.recv(1024).decode()
    print(f'Received echo back: {data}')
