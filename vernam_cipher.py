import string
import random

def string_mapping():
    str_to_int, int_to_str = {}, {}
    for int_ in range(len(string.printable)):
        int_to_str[int_] = string.printable[int_]
        str_to_int[string.printable[int_]] = int_
        
    return str_to_int, int_to_str

def one_time_pad(org_msg):
    key = ''
    for i in range(len(org_msg)):
        key += random.choice(string.printable)
    return key

def encrypt_to_vernam_cipher(org_msg, key, str_to_int, int_to_str):
    cipher_txt = ''
    for idx, str_ in enumerate(org_msg):
        new_int = (str_to_int[str_] + str_to_int[key[idx]]) % 100
        new_str = int_to_str[new_int]
        cipher_txt += new_str
    return cipher_txt

def decrypte_to_org_msg(cipher_txt, key, str_to_int, int_to_str):
    org_txt = ''
    for idx, str_ in enumerate(cipher_txt):
        new_int = (str_to_int[str_] - str_to_int[key[idx]]) % 100
        new_str = int_to_str[new_int]
        org_txt += new_str
    return org_txt

if __name__ == '__main__':
    str_to_int, int_to_str = string_mapping()
    txt = ('''
            It was difficult for Mary to admit that most of her workout consisted of exercising poor judgment.
            Random words in front of other random words create a random sentence.
            I may struggle with geography, but I'm sure I'm somewhere around here.
            She had the gift of being able to paint songs.
            The tattered work gloves speak of the many hours of hard labor he endured throughout his life.
           ''')
    key = one_time_pad(txt)
    print("Original Text : \n", txt)
    cipher = encrypt_to_vernam_cipher(txt, key, str_to_int, int_to_str)
    print("Encrypted Text : \n", cipher)
    org_txt = decrypte_to_org_msg(cipher, key, str_to_int, int_to_str)
    print("Decrypted Text : \n", org_txt)