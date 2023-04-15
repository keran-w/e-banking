import socket, time

class SSS(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        super().__init__(family, type, proto, fileno)
        self.last_active = time.time()

    def SENDALL(self, data):
        self.last_active = time.time()
        return super().sendall(data)

    def RECV(self, data):
        self.last_active = time.time()
        return super().recv(data)