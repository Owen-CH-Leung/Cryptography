import string
import random

def string_mapping():
    str_to_int, int_to_str = {}, {}
    for int_ in range(len(string.printable)):
        int_to_str[int_] = string.printable[int_]
        str_to_int[string.printable[int_]] = int_
        
    return str_to_int, int_to_str

def get_key(length):
    key = ''
    for i in range(length):
        key += random.choice(string.printable)
    return key

def encrypt_to_vigenere_cipher(org_msg, key, str_to_int, int_to_str):
    cipher_txt = ''
    key_idx = 0
    for str_ in org_msg:
        new_int = (str_to_int[str_] + str_to_int[key[key_idx]]) % 100
        new_str = int_to_str[new_int]
        cipher_txt += new_str
        key_idx += 1
        if key_idx == len(key):
            key_idx = 0
    return cipher_txt

def decrypte_to_org_msg(cipher_txt, key, str_to_int, int_to_str):
    org_txt = ''
    key_idx = 0
    for str_ in cipher_txt:
        new_int = (str_to_int[str_] - str_to_int[key[key_idx]]) % 100
        new_str = int_to_str[new_int]
        org_txt += new_str
        key_idx += 1
        if key_idx == len(key):
            key_idx = 0
    return org_txt

if __name__ == '__main__':
    str_to_int, int_to_str = string_mapping()
    key = get_key(10)
    txt = ('''
            The external scars tell only part of the story.
            Never underestimate the willingness of the greedy to throw you under the bus.
            He had reached the point where he was paranoid about being paranoid.
           ''')
    print("Original Text : \n", txt)
    cipher = encrypt_to_vigenere_cipher(txt, key, str_to_int, int_to_str)
    print("Encrypted Text : \n", cipher)
    org_txt = decrypte_to_org_msg(cipher, key, str_to_int, int_to_str)
    print("Decrypted Text : \n", org_txt)