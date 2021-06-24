import string
import random

def string_mapping():
    str_to_int, int_to_str = {}, {}
    for int_ in range(len(string.printable)):
        int_to_str[int_] = string.printable[int_]
        str_to_int[string.printable[int_]] = int_
        
    return str_to_int, int_to_str

def get_key(lower, upper):
    return random.randint(lower, upper)

def encrypt_to_caesar_cipher(org_msg, key, str_to_int, int_to_str):
    cipher_txt = ''
    for str_ in org_msg:
        new_int = (str_to_int[str_] + key) % 100
        new_str = int_to_str[new_int]
        cipher_txt += new_str
    return cipher_txt

def decrypte_to_org_msg(cipher_txt, key, str_to_int, int_to_str):
    org_txt = ''
    for str_ in cipher_txt:
        new_int = (str_to_int[str_] - key) % 100
        new_str = int_to_str[new_int]
        org_txt += new_str            
    return org_txt

def crack_caesar_brute_force(cipher_txt, str_to_int, int_to_str):
    for key in range(len(string.printable)):
        txt = ''
        for str_ in cipher_txt:
            new_int = (str_to_int[str_] - key) % 100
            new_str = int_to_str[new_int]
            txt += new_str    
        print(f"With Key {key}, the decrypted text is : \n {txt}")
    
    
if __name__ == '__main__':
    str_to_int, int_to_str = string_mapping()
    key = get_key(0, 100)
    txt = ('''
           Hong Kong is a metropolitan area and special administrative region of China on the eastern 
           Pearl River Delta in South China.
           ''')
    print("Original Text : \n", txt)
    cipher = encrypt_to_caesar_cipher(txt, key, str_to_int, int_to_str)
    print("Encrypted Text : \n", cipher)
    org_txt = decrypte_to_org_msg(cipher, key, str_to_int, int_to_str)
    print("Decrypted Text : \n", org_txt)
    crack_caesar_brute_force(cipher, str_to_int, int_to_str)