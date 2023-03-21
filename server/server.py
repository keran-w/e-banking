import socket, threading, sys, decimal

MESSAGE_LENGTH = 1024
PORT = 12345
MAX_CONNECTION = 5

# Global dictionary to store account information
# username : password
accounts = {}
# Global dictionary to store logged in users and their sockets
# username : socket
logged_in_users = {}
# Global dictionary to store user balances
# username : balance
balances = {}

# Returns a message indicating whether this operation is successful
def create_account(command):
    username = command[1]
    password = command[2]
    # Check if account with same name already exists
    if username in accounts:
        return("Error: Account already exists.")
    else:
        accounts[username] = password
        balances[username] = 0
        return("Account created successfully.")

# Returns [username(empty string if not successful), Message] indicating whether this operation is successful
def login(command):
    username = command[1]
    password = command[2]
    if username not in accounts:
        return(["", "Error: Account does not exist."])
    elif username in logged_in_users:
        return(["", "Error: Account already logged in."])
    elif accounts[username] != password:
        return(["", "Error: Incorrect password."])
    else:
        logged_in_users[username] = client_socket
        return([username, "Login successful."])
    
# Closes the socket and removes the user's session 
def close_client_socket(socket, user):
    # Close client socket
    socket.close()
    # Remove user from logged_in_users dictionary upon disconnect
    for user in logged_in_users.copy():
        if logged_in_users[user] == socket:
            del logged_in_users[user]

    



def handle_client(client_socket):
    # The currect session user
    user = ""

    while True:
        data = client_socket.recv(MESSAGE_LENGTH).decode()
        command = data.split()
        feedback = ""

        if not user:
            if command[0] == "create_account" or command[0] == "c":
                feedback = create_account(command)

            elif command[0] == "login" or command[0] == "l":
                user, feedback = login(command)

        else:
            print(f'{user}: {data}')

            if command[0] == "exit":
                close_client_socket(client_socket, user)
                return

            elif command[0] == "balance":
                feedback = str(balances[user])

            elif command[0] == "withdraw" and len(command) == 2 and command[1].isdecimal():
                amount = decimal.Decimal(command[1])
                if amount <= balances[user]:
                    feedback = "Success"
                    balances[user] -= amount
                else:
                    feedback = "Insufficient Balance"

            elif command[0] == "deposit" and len(command) == 2 and command[1].isdecimal():
                balances[user] += decimal.Decimal(command[1])
                feedback = "Success"

            else:
                feedback = "Invalid Operations"
        
        client_socket.sendall(feedback.encode())

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))
server_socket.listen(MAX_CONNECTION)
print(f'Server is listening on port {PORT}...')

# Handle incoming client connections
while True:
    client_socket, addr = server_socket.accept()
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
