import socket, sys

MESSAGE_LENGTH = 1024
PORT = 12345

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', PORT))

# account creation or login
if len(sys.argv) == 2 and sys.argv[1] == "-dev":
   create_dev_account = "c dev 114514"
   login_dev_account = "l dev 114514"
   client_socket.sendall(create_dev_account.encode())
   response = client_socket.recv(MESSAGE_LENGTH).decode()
   print(response)
   client_socket.sendall(login_dev_account.encode())
   response = client_socket.recv(MESSAGE_LENGTH).decode()
   print(response)

else:
    while True:
        user_input = input("Enter 'create_account <username> <password>' to create an account\n"
                           "Enter 'login <username> <password>' to log in to an account\n")
        client_socket.sendall(user_input.encode())
        response = client_socket.recv(MESSAGE_LENGTH).decode()
        print(response)
        if response == "Login successful.":
            break

print("Operations: \t withdraw [$] \n\t\t deposit [$] \n\t\t balance \n\t\t exit")
# Send messages to server
while True:
    message = input('Enter a message to send to the server: ')
    if len(message) > MESSAGE_LENGTH:
        print("Invalid message")

    if message == "exit":
        client_socket.close()
        exit()

#     else if message[:len(8)] == "withdraw":

#     else if message[:len(7)] == "deposit":
#
    else if message[:len(7)] == "balance":

    else:
        print("Invalid message")
        continue

    client_socket.sendall(message.encode())
    data = client_socket.recv(MESSAGE_LENGTH).decode()
    print(f'Received: {data}')
