from des import DES
import socket
import time


class SSS(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        super().__init__(family, type, proto, fileno)
        self.last_active = time.time()
        # self.cipher = DES('10010011')

    def SENDALL(self, data: bytes, key):
        # assert len(data) % 8 == 0
        # self.last_active = time.time()
        # des = DES(key)
        # des.proc(data.encode('ascii'), 'ENC')
        # return super().sendall(data)

        # data = b'abc'
        des = DES(key)
        data_ = ''.join([bin(ord(c))[2:].zfill(8) for c in data.decode()])
        return super().sendall(des.proc(data_.encode(), 'ENC'))

    def RECV(self, data, key):
        self.last_active = time.time()
        des = DES(key)
        p = des.proc(data, 'DEC').decode()
        p = ''.join([chr(int(p[i:i+8], 2)) for i in range(0, len(p), 8)])
        return super().recv(p.encode())
