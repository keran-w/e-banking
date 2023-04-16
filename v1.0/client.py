import socket, sys, pickle, time
import util
import supersecuresocket as SSS

MESSAGE_LENGTH = 67136
PORT = 12345
SESSION_TIME = 300

def login(session_key):
    while True:
        user_input = input("Enter 'create_account <username> <password>' to create an account\n"
                           "Enter 'login <username> <password>' to log in to an account\n")

        words = user_input.split()
        if len(words) != 3:
            print("Invalid")
            continue
        if words[0] == "c" or words[0] == "create_account":
            if not util.is_password_complex(words[2]):
                print("The password must be at least 8 characters long.\nThe password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                continue

        client_socket.SENDALL(user_input.encode(), session_key)
        response = client_socket.RECV(MESSAGE_LENGTH, session_key).decode()
        print(response)
        if response == "Login successful.":
            break

def operations(session_key):
    while(True):
        message = input('Enter a message to send to the server: ')
        if(time.time() - client_socket.last_active > SESSION_TIME):
            print("Session timed out due to inactivity.")
            message = ""
            break

        if len(message) > MESSAGE_LENGTH:
            print("Invalid message")

        else:
            client_socket.SENDALL(message.encode(), session_key)
            data = client_socket.RECV(MESSAGE_LENGTH, session_key).decode()
            print(f'Received: {data}')

        if message == "exit":
            client_socket.close()
            exit()

print(f'Client initializing ...')
while(True):
    client_socket = SSS.SSS(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    session_key = util.generate_prime_number(1024);
    server_rsa_publickey = pickle.loads(client_socket.recv(MESSAGE_LENGTH))
    client_socket.sendall(pickle.dumps(util.rsa_encrypt(server_rsa_publickey, str(session_key))))

    login(session_key)
    print("Operations: \t withdraw [$] \n\t\t deposit [$] \n\t\t balance \n\t\t exit")
    operations(session_key)


