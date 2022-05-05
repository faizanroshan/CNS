import random
import math

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def pow(m, e, n):

    if e == 0:
        return 1
    elif e == 1:
        return m % n
    else:
        return (m ** e) % n

def RSA(m):

    # Generate p and q
    p = 251
    q = 389
    
    n = p * q

    phi = (p - 1) * (q - 1)

    e = 0
    while e == 0:
        e = random.randint(2, phi)
        if math.gcd(e, phi) != 1:
            e = 0

    d = 0
    while d == 0:
        d = modinv(e, phi)

    # Encrypt
    c = pow(m, e, n)

    # Decrypt
    m = pow(c, d, n)
    print("Encrypted message:", c)
    print("Decrypted message:", m)
    return m, n, e, d

if __name__ == "__main__":
    m = int(input("Enter a message: "))
    m, n, e, d = RSA(m)
    print("Public key:", n, e)
    print("Private key:", n, d)