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

def generate_keypair():
    num_bits = 512
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


# def rsa_encrypt(public_key, plaintext):
#     key, n = public_key
#     cipher = [pow(ord(char), key, n) for char in plaintext]
#     return cipher

def rsa_decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)
