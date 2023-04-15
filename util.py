import math, random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_number(num_bits):
    while True:
        p = random.getrandbits(num_bits)
        p |= (1 << num_bits - 1) | 1  # set the most significant and least significant bits
        if is_prime(p):
            return p

def generate_keypair(num_bits):
    p = generate_prime_number(num_bits)
    q = generate_prime_number(num_bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))


def rsa_encrypt(public_key, plaintext):
    key, n = public_key
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def rsa_decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def sha1(data):
    # Step 1: Prepare the message
    padding = b"\x80" + b"\x00" * (63 - (len(data) + 8) % 64)
    length = len(data) * 8
    message = data + padding + length.to_bytes(8, byteorder="big")

    # Step 2: Initialize the hash
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Step 3: Process the message in 512-bit chunks
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        words = [int.from_bytes(chunk[j:j+4], byteorder="big") for j in range(0, 64, 4)]
        for j in range(16, 80):
            word = words[j-3] ^ words[j-8] ^ words[j-14] ^ words[j-16]
            words.append((word << 1) | (word >> 31))
        a, b, c, d, e = h0, h1, h2, h3, h4
        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = ((a << 5) | (a >> 27)) + f + e + k + words[j] & 0xFFFFFFFF
            e = d
            d = c
            c = (b << 30) | (b >> 2)
            b = a
            a = temp
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Step 4: Return the hash value
    return (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4