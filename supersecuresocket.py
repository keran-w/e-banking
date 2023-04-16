import time
import socket
from cipher import HMAC


class SSS(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        super().__init__(family, type, proto, fileno)
        self.last_active = time.time()

    def SENDALL(self, data: bytes, key: bytes):
        self.hmac = HMAC(key, data)
        cipher_text = self.hmac.encrypt()
        return super().sendall(cipher_text)

    def RECV(self, length: bytes, key: bytes):
        self.last_active = time.time()
        cipher_text = super().recv(length)
        assert self.hmac.key == key
        return self.hmac.decrypt(cipher_text)
