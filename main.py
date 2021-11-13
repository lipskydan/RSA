import rsa
import rsa_oaep

if __name__ == '__main__':
    plaintext = "Hello World"
    print(f'plaintext = {plaintext}')
    public, private = rsa.new_key_pair(512)

    ciphertext_rsa = rsa.encrypt(plaintext.encode('utf-8'), public)
    print(f'RSA encryption: {ciphertext_rsa}')
    decryptedtext_rsa = rsa.decrypt(ciphertext_rsa, private)
    print(f'RSA decryption: {decryptedtext_rsa.decode("utf-8")}')

    ciphertext_rsa_oaep = rsa_oaep.encrypt(plaintext.encode('utf-8'), public)
    print(f'RSA OAEP encryption: {ciphertext_rsa_oaep}')
    decryptedtext_rsa_oaep = rsa_oaep.decrypt(ciphertext_rsa_oaep, private)
    print(f'RSA OAEP decryption: {decryptedtext_rsa_oaep.decode("utf-8")}')

