# import secrets
# from rsa_help import *
#
#
# def generate_prime(n):
#     p = int(secrets.token_hex(n), 16)
#     while not is_prime(p):
#         if p % 2 == 0:
#             p += 1
#         else:
#             p += 2
#     q = int(secrets.token_hex(n), 16)
#     while not is_prime(q) or p == q:
#         if q % 2 == 0:
#             q += 1
#         else:
#             q += 2
#     return [p, q]
#
#
# def generate_key(lens):
#     p, q = generate_prime(lens)
#     n = p * q
#     e = 65537
#     phi = (p - 1) * (q - 1)
#     d = get_inv(e, phi)
#     return [[p, q], [n, e], [phi, d]]
#
#
# def encrypt(plaintext, n, e):
#     if plaintext > n - 1:
#         raise IndexError(
#             'You are trying to encrypt a message with invalid length.')
#     return fast_pow(plaintext, e, n)
#
#
# def decrypt(ciphertext, p, q, d):
#     cipher_p = ciphertext % p
#     cipher_q = ciphertext % q
#     d_p = d % (p - 1)
#     d_q = d % (q - 1)
#     x_p = fast_pow(cipher_p, d_p, p)
#     x_q = fast_pow(cipher_q, d_q, q)
#     return crt([[p, x_p], [q, x_q]])
#
#
# def decrypt_without_pq(ciphertext, n, d):
#     return fast_pow(ciphertext, d, n)
#
#
# def main():
#     pq, pub, pri = generate_key(128)
#     ciphertext = encrypt(0x92374924d23497ad329487129, pub[0], pub[1])
#     print(ciphertext)
#     print(hex(decrypt(ciphertext, pq[0], pq[1], pri[1])))
#
# if __name__ == '__main__':
#     main()

import math
import random

from helpers import new_prime, mul_inv, bytes_to_int, int_to_bytes


def _choose_e(phi_n):
    while True:
        e = random.randint(3, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            return e


def new_key_pair(num_bits):
    p = new_prime(num_bits)
    q = new_prime(num_bits)
    N = p * q
    phi_N = (p - 1) * (q - 1)
    e = _choose_e(phi_N)
    d = mul_inv(e, phi_N)
    d_p = d % (p - 1)
    d_q = d % (q - 1)
    q_inv = mul_inv(q, p)
    return (N, e), (p, q, d_p, d_q, q_inv)


def encrypt(plaintext, public_key):
    N, e = public_key
    m = bytes_to_int(plaintext)
    assert m < N
    c = pow(m, e, N)
    return int_to_bytes(c)


def decrypt(ciphertext, private_key):
    p, q, d_p, d_q, q_inv = private_key
    c = bytes_to_int(ciphertext)
    m1 = pow(c, d_p, p)
    m2 = pow(c, d_q, q)
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % (p * q)
    return int_to_bytes(m)