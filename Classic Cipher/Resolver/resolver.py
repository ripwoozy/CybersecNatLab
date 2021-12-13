import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
keys = []
cryptedtext = "xcqvgvyavnzvztvetvtddlnxcgy"

def generateKey():
    for x in range(26):
        if x == 0:
            continue
        key = "".join([alphabet[x:], alphabet[0:x]])
        keys.append(key)


def decrypt(ct,key):
    cryptedtext = ""
    for k in range(len(ct)):
        character = ct[k]
        lmao = key.index(character)
        decryptedchar = alphabet[lmao]
        key = "".join([key[len(key)-1:],key[0:len(key)-1]])
        cryptedtext = "".join([cryptedtext,decryptedchar])
    print(f"KEY: {key} DECRYPTED TEXT: {cryptedtext} ")


generateKey()
for key in keys:
    decrypt(cryptedtext, key)