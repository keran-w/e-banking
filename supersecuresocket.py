import socket

class SSS(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        super().__init__(family, type, proto, fileno)

    def SENDALL(self, data):
        return super().sendall(data)

    def RECV(self, data):
        return super().recv(data)

    # def RECV(self):
#
# class SSS_fd():
#     def SENDALL(self, data):
#         super().sendall(data)