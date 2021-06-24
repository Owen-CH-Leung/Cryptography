from Crypto.Cipher import AES
import string
import random
import binascii
from Crypto import Random

def pad(string_, ):
    new_str = string_
    n_pad = 0
    if len(new_str) % 128 != 0:
        for i in range(128 - (len(new_str) % 128)):
            new_str += random.choice(string.printable)
            n_pad += 1
        return new_str, n_pad
    else:
        return new_str, n_pad

def remove_pad(new_str, n_pad):
    rm_str = new_str
    for i in range(n_pad):
        rm_str = rm_str[:-1]
        
    return rm_str

def encrypt(plaintext, key):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(plaintext)

def decrypt(ciphertext, key):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.decrypt(ciphertext).decode('UTF-8')


if __name__ == "__main__":

	key = key = Random.new().read(16)
	plaintext = """The following secret message needs to be encrypted : 
        People who insist on picking their teeth with their elbows are so annoying!"""
	new_plaintext, n_pad = pad(plaintext)
	
	ciphertext = encrypt(new_plaintext.encode('utf-8'), key)
	print(binascii.hexlify(bytearray(ciphertext)))
	
	decrypted = decrypt(ciphertext,key)
	decrypted = remove_pad(decrypted, n_pad)
	print("Decrypted message:" ,decrypted)
	