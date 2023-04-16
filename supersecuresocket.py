import time
import socket
from cipher import DESHMAC


class SSS(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        super().__init__(family, type, proto, fileno)
        self.last_active = time.time()

    def SENDALL(self, data: bytes, key: bytes) -> None:
        cipher_text = DESHMAC(key).encrypt(data)
        return super().sendall(cipher_text)

    def RECV(self, length: bytes, key: bytes) -> bytes:
        self.last_active = time.time()
        cipher_text = super().recv(length)
        return DESHMAC(key).decrypt(cipher_text)
