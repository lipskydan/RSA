import rsa
import rsa_oaep
from helpers import miller_rabin


def miller_rabin_show(n, k):
    if miller_rabin(n, k):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')


if __name__ == '__main__':
    k = 40
    a = 5988382547900011059982773127027433035392095026839118950463435933621301606863651092678197998843867907
    b = 6676066668704114317437996979438473867662389657659641149291788326199361365713977263095493680135216599
    c = a*b

    miller_rabin_show(3, k)
    miller_rabin_show(6, k)
    miller_rabin_show(a, k)
    miller_rabin_show(c, k)

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
