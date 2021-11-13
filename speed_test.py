import os
import time

import rsa
import rsa_oaep

for bit_length in [512, 1024]:
    print(f'p and q bit length: {bit_length}')
    m_len = bit_length // 4 - 66
    print(f'Message bit length: {m_len * 8}')
    plaintext = os.urandom(m_len)
    public, private = rsa.new_key_pair(bit_length)

    start = time.time()
    ciphertext = rsa.encrypt(plaintext, public)
    print(f'RSA encryption took: {time.time() - start:.4} s')
    start = time.time()
    rsa.decrypt(ciphertext, private)
    print(f'RSA decryption took: {time.time() - start:.4} s')

    start = time.time()
    ciphertext = rsa_oaep.encrypt(plaintext, public)
    print(f'RSA-OAEP encryption took: {time.time() - start:.4} s')
    start = time.time()
    rsa_oaep.decrypt(ciphertext, private)
    print(f'RSA-OAEP decryption took: {time.time() - start:.4} s')
    print()