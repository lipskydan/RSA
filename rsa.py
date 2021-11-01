import secrets
from rsa_help import *


def generate_prime(n):
    p = int(secrets.token_hex(n), 16)
    while not is_prime(p):
        if p % 2 == 0:
            p += 1
        else:
            p += 2
    q = int(secrets.token_hex(n), 16)
    while not is_prime(q) or p == q:
        if q % 2 == 0:
            q += 1
        else:
            q += 2
    return [p, q]


def generate_key(lens):
    p, q = generate_prime(lens)
    n = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
    d = get_inv(e, phi)
    return [[p, q], [n, e], [phi, d]]


def encrypt(plaintext, n, e):
    if plaintext > n - 1:
        raise IndexError(
            'You are trying to encrypt a message with invalid length.')
    return fast_pow(plaintext, e, n)


def decrypt(ciphertext, p, q, d):
    cipher_p = ciphertext % p
    cipher_q = ciphertext % q
    d_p = d % (p - 1)
    d_q = d % (q - 1)
    x_p = fast_pow(cipher_p, d_p, p)
    x_q = fast_pow(cipher_q, d_q, q)
    return crt([[p, x_p], [q, x_q]])


def decrypt_without_pq(ciphertext, n, d):
    return fast_pow(ciphertext, d, n)


def main():
    pq, pub, pri = generate_key(128)
    ciphertext = encrypt(0x92374924d23497ad329487129, pub[0], pub[1])
    print(ciphertext)
    print(hex(decrypt(ciphertext, pq[0], pq[1], pri[1])))


if __name__ == '__main__':
    main()