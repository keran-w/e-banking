from des import DES
import socket
import time


class SSS(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        super().__init__(family, type, proto, fileno)
        self.last_active = time.time()

    def SENDALL(self, data: bytes, key):
        des = DES(str(key))
        data_ = ''.join([bin(ord(c))[2:].zfill(8) for c in data.decode()])
        return super().sendall(des.proc(data_.encode(), 'ENC'))

    def RECV(self, length, key):
        self.last_active = time.time()
        cipher = super().recv(length)
        des = DES(str(key))
        p = des.proc(cipher, 'DEC').decode()
        p = ''.join([chr(int(p[i:i+8], 2)) for i in range(0, len(p), 8)])
        return p.encode()
