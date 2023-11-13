import hashlib
import math
import pyperclip
import binascii
import pandas as pd
import eel

eel.init("web")

@eel.expose
def cypher_hk(text_c, shift, code, cypher_type):
    def caesar_code(shift_c, text):
        result = ""
        for i in range(len(text)):
            char_t = text[i]
            if char_t == ' ':
                result+= ' '
            elif char_t.isupper():
                result += chr((ord(char_t) + shift_c - 65) % 26 + 65)
            else:
                result += chr((ord(char_t) + shift_c - 97) % 26 + 97)
        return result

    def generateKey(str_c, key):
        key = list(key)
        if len(str_c) == len(key):
            return (key)
        else:
            for i in range(len(str_c) -
                           len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

    def cipherText(str_c, key):
        Cipher_Text = []
        for i in range(len(str_c)):
            x = (ord(str_c[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            Cipher_Text.append(chr(x))
        return ("".join(Cipher_Text))

    def originalText(Cipher_Text, key):
        str_c = []
        for i in range(len(Cipher_Text)):
            x = (ord(Cipher_Text[i]) -
                 ord(key[i]) + 26) % 26
            x += ord('A')
            str_c.append(chr(x))
        return ("".join(str_c))

    c_t = int(cypher_type)
    s = shift
    c = int(code)
    if c_t == 1 and s.isalpha():
        return "Ошибка! Введите положительное число."
    if c_t == 1:
        if int(s) >= 0:
            if c == 1:
                return caesar_code(int(s), text_c)
            elif c == 2:
                return caesar_code(-int(s), text_c)
        else:
            return "Ошибка! Шаг не может быть отрицательным числом."
    if c_t == 2:
        if c == 1:
            if __name__ == "__main__":
                key = generateKey(text_c, s)
                cipher_text = cipherText(text_c, key)
                return cipher_text

        elif c == 2:
            if __name__ == "__main__":
                key = generateKey(text_c, s)
                return originalText(text_c, key)


@eel.expose
def cypher_nk(text_c, cypher_type):
    cypher_t = int(cypher_type)

    def SHA1(text):
        result = hashlib.sha1(text.encode())
        return result.hexdigest()

    def SHA256(text):
        result = hashlib.sha256(text.encode())
        return result.hexdigest()

    def SHA512(text):
        result = hashlib.sha512(text.encode())
        return result.hexdigest()

    def MD5(text):
        result = hashlib.md5(text.encode())
        return result.hexdigest()

    if cypher_t == 2:
        return SHA1(text_c)
    if cypher_t == 3:
        return SHA256(text_c)
    if cypher_t == 4:
        return SHA512(text_c)
    if cypher_t == 5:
        return MD5(text_c)

@eel.expose
def cypher_bin(text_c, cypher_type, type):
    def t_to_bin(text):
        text_2_bin = bin(int.from_bytes(text.encode(), 'big'))[2:]
        return text_2_bin
    def bin_to_t(text):
        dec = int(text, 2)
        bin_2_text = dec.to_bytes((dec.bit_length() + 7) // 8, 'big').decode()
        return bin_2_text

    def str2hex(s):
        return binascii.hexlify(bytes(str.encode(s)))

    def hex2str(s):
        return binascii.unhexlify(s)

    type_code = int(type)
    cypher_t = int(cypher_type)
    if cypher_t == 1:
        if type_code == 1:
            return t_to_bin(text_c)
        if type_code == 2:
            return bin_to_t(text_c)
    if cypher_t == 4:
        if type_code == 1:
            hexstring = str2hex(text_c)
            return hexstring.decode('utf-8')
        if type_code == 2:
            unhexsring = hex2str(text_c).decode('utf-8')
            return unhexsring

eel.start("index_have_key.html", size=(324, 619), mode="chrome")



