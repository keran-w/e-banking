import struct
import numpy as np

# Static Variables

# The SBOX table used in DES encryption and decryption
SBOX = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]

# Initial Permutation
IP = [
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6
]

# Permutation after F
P = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30,
     9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24]

# Permuted Choice 1
PC1 = [
    56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3
]

# Permuted Choice 2
PC2 = [
    13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40,
    51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31
]

# Final Permutation
FP = [
    39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25, 32, 0, 40, 8, 48, 16, 56, 24
]

# Expansion
EXP = [
    31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15,
    16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0
]


class SHA1:
    # Reference: https://gist.github.com/BenWiederhake/cb60f703840f9e81a84499b39eb361b5

    def __init__(self, data=b''):
        self.h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]
        self.remainder = data
        self.count = 0

    def _leftrotate(self, i, n):
        return ((i << n) & 0xffffffff) | (i >> (32 - n))

    def _add_chunk(self, chunk):
        self.count += 1
        w = list(struct.unpack(">16I", chunk) + (None,) * (80-16))
        for i in range(16, 80):
            n = w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]
            w[i] = self._leftrotate(n, 1)
        a, b, c, d, e = self.h
        for i in range(80):
            f = None
            k = None
            if i < 20:
                f = (b & c) ^ (~b & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) ^ (b & d) ^ (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (self._leftrotate(a, 5) + f + e + k + w[i]) % 2**32
            e = d
            d = c
            c = self._leftrotate(b, 30)
            b = a
            a = temp
        self.h[0] = (self.h[0] + a) % 2**32
        self.h[1] = (self.h[1] + b) % 2**32
        self.h[2] = (self.h[2] + c) % 2**32
        self.h[3] = (self.h[3] + d) % 2**32
        self.h[4] = (self.h[4] + e) % 2**32

    def add(self, data):
        message = self.remainder + data
        r = len(message) % 64
        if r != 0:
            self.remainder = message[-r:]
        else:
            self.remainder = b''
        for chunk in range(0, len(message)-r, 64):
            self._add_chunk(message[chunk:chunk+64])
        return self

    def finish(self):
        l = len(self.remainder) + 64 * self.count
        self.add(b'\x80' + b'\x00' * ((55 - l) %
                 64) + struct.pack(">Q", l * 8))
        h = tuple(x for x in self.h)
        self.__init__()
        return struct.pack(">5I", *h)


# Helper Functions for DES
permute = lambda P, arr: [arr[i] for i in P]
str2bit = lambda str10: [int(i) for dec in str10 for i in bin(dec)[2:].zfill(8)]
bit2str = lambda str2: bytes([int(''.join([str(i) for i in arr]), 2) for arr in np.array_split(str2, len(str2)//8)])
xor = lambda arr1, arr2: list(np.logical_xor(arr1, arr2).astype('int'))
bin2dec = lambda arr2: int(''.join([str(i) for i in arr2]), 2)
unpack_bits = lambda bits: np.unpackbits(np.array([bits], dtype=np.uint8))[4:]


class DES:

    def __init__(self, key):
        self.key = key.encode('ascii')

    def des(self, text):
        left_half, right_half = np.array_split(permute(IP, text), 2)

        for _ in range(16) if self.mode == 'ENC' else reversed(range(16)):
            right_half_ = permute(EXP, right_half)
            blocks = np.array_split(right_half_, 8)
            block_bits = np.zeros(32, dtype=int)
            for j in range(8):
                m, n = bin2dec(blocks[j][0:2]), bin2dec(blocks[j][1:5])
                block_bits[4*j:4*j+4] = unpack_bits(SBOX[j][m*16+n])

            right_half_ = xor(permute(P, block_bits), left_half)
            left_half, right_half = right_half, right_half_

        return permute(FP, right_half+left_half)

    def proc(self, text, mode):
        self.mode = mode
        res = [self.des(str2bit(text[i:i+8])) for i in range(0, len(text), 8)]
        return bit2str([j for i in res for j in i])

def hmac_sha1(key, message):
    key = list(key + b'\x00' * (64 - len(key)))
    inner_key = bytes([a ^ b for a, b in zip(key, bytes([0x36] * 64))])
    outer_key = bytes([a ^ b for a, b in zip(key, bytes([0x5c] * 64))])    
    inner_hash = SHA1(inner_key + message).finish()
    outer_hash = SHA1(outer_key + inner_hash).finish()
    return outer_hash

class HMAC:
    def __init__(self, key, message):
        self.key = key
        self.message = message
        self.DES = DES(key.decode())
        self._preproc()
        
    def _preproc(self):
        self.hmac_key = SHA1(self.key).finish()
        self.signature = hmac_sha1(self.hmac_key, self.message)
        concat_message = message + self.signature.hex().encode()
        self.concat_message = ''.join([bin(ord(c))[2:].zfill(8) for c in concat_message.decode()])
        
    def encrypt(self):
        return self.DES.proc(self.concat_message.encode(), 'ENC')
    
    def decrypt(self, cipher_text):
        try:
            dec_text = self.DES.proc(cipher_text, 'DEC').decode()
            dec_msg = ''.join([chr(int(dec_text[i:i+8],2)) for i in range(0, len(dec_text), 8)])
            message_, signature_ = dec_msg[:-40], dec_msg[-40:]
            if signature_ == self.signature.hex():
                return message_
            else:
                return b''
        except:
            return b''
            
        

if __name__ == '__main__':
    # test sha1
    msg = b'Nobody inspects the spammish repetition'
    import hashlib
    assert hashlib.sha1(msg).hexdigest() == SHA1(msg).finish().hex()

    # test des
    des = DES('10010011')
    c = des.proc('100100011001011110011001'.encode('ascii'), 'ENC')
    assert str(des.proc(c, 'DEC'))[2:-1] == '100100011001011110011001'

    des = DES('10011111')
    c = des.proc('110100011001011110011001'.encode('ascii'), 'ENC')
    assert str(des.proc(c, 'DEC'))[2:-1] == '110100011001011110011001'
    
    # example 
    message = b'withdraw 100 dollars'
    secret_key = b'theSecretKey'
    hmac_key = SHA1(secret_key).finish()
    import hmac
    hmac_value = hmac_sha1(hmac_key, message)
    assert hmac_value == hmac.new(hashlib.sha1(secret_key).digest(), message, hashlib.sha1).digest()
    
    concat_message = message + hmac_value.hex().encode()
    concat_message = ''.join([bin(ord(c))[2:].zfill(8) for c in concat_message.decode()])
    cipher_text = DES(secret_key.decode()).proc(concat_message.encode(), 'ENC')
    dec_text = DES(secret_key.decode()).proc(cipher_text, 'DEC').decode()
    dec_msg = ''.join([chr(int(dec_text[i:i+8],2)) for i in range(0, len(dec_text), 8)])
    message_, hmac_value_ = dec_msg[:-40], dec_msg[-40:]

    assert hmac_value_ == hmac_value.hex()
    assert message_ == message.decode()
    
    # test hmac
    message = b'withdraw 100 dollars'
    secret_key = b'theSecretKey'
    hmac = HMAC(secret_key, message)
    cipher_text = hmac.encrypt()
    
    # test a valid cipher text
    message_ = hmac.decrypt(cipher_text)
    assert message_ == message.decode()
    
    # test an invalid cipher text
    cipher_text_2 = cipher_text[:-1] + b'\x2e'
    message_2 = hmac.decrypt(cipher_text_2)
    assert message_2 == b''