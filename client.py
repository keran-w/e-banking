import socket, sys, pickle
import util
import supersecuresocket as SSS

MESSAGE_LENGTH = 1024
PORT = 12345

# Set up client socket
client_socket = SSS.SSS(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', PORT))

# symm_key setup
session_key = util.generate_prime_number(16);
server_rsa_publickey = pickle.loads(client_socket.RECV(MESSAGE_LENGTH))
client_socket.SENDALL(pickle.dumps(util.rsa_encrypt(server_rsa_publickey, str(session_key))))

# account creation or login
if len(sys.argv) == 2 and sys.argv[1] == "-dev":
    create_dev_account = "c dev 114514"
    login_dev_account = "l dev 114514"
    client_socket.SENDALL(create_dev_account.encode())
    response = client_socket.RECV(MESSAGE_LENGTH).decode()
    print(response)
    client_socket.SENDALL(login_dev_account.encode())
    response = client_socket.RECV(MESSAGE_LENGTH).decode()
    print(response)

else:
    while True:
        user_input = input("Enter 'create_account <username> <password>' to create an account\n"
                           "Enter 'login <username> <password>' to log in to an account\n")
        client_socket.SENDALL(user_input.encode())
        response = client_socket.RECV(MESSAGE_LENGTH).decode()
        print(response)
        if response == "Login successful.":
            break

print("Operations: \t withdraw [$] \n\t\t deposit [$] \n\t\t balance \n\t\t exit")
# Send messages to server
while True:
    message = input('Enter a message to send to the server: ')
    if len(message) > MESSAGE_LENGTH:
        print("Invalid message")

    else:
        client_socket.SENDALL(message.encode())
        data = client_socket.RECV(MESSAGE_LENGTH).decode()
        print(f'Received: {data}')

    if message == "exit":
        client_socket.close()
        exit()


