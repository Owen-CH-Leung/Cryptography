from Crypto.Cipher import DES
import string
import random
import binascii

def generate_8byte_key():
    key = ''
    for _ in range(8):
        key += random.choice(string.printable)
	
    return key

def pad(string_):
    new_str = string_
    n_pad = 0
    if len(new_str) % 8 != 0:
        for i in range(8 - (len(new_str) % 8)):
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

def encrypt(plaintext, key, mode = DES.MODE_ECB):
	des = DES.new(key, mode)
	return des.encrypt(plaintext)

def decrypt(ciphertext, key, mode = DES.MODE_ECB):
	des = DES.new(key, mode)
	return des.decrypt(ciphertext).decode('UTF-8')


if __name__ == "__main__":

	key = generate_8byte_key()
	plaintext = """The following secret message needs to be encrypted : 
        People who insist on picking their teeth with their elbows are so annoying!"""
	new_plaintext, n_pad = pad(plaintext)
	
	ciphertext = encrypt(new_plaintext.encode('utf-8'), key.encode('utf-8'))
	print(binascii.hexlify(bytearray(ciphertext)))
	
	decrypted = decrypt(ciphertext,key.encode('utf-8'))
	decrypted = remove_pad(decrypted, n_pad)
	print("Decrypted message:" ,decrypted)
	