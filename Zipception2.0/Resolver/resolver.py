from zipfile import ZipFile
# ----------------------------------------------------------
wordlist = "passw.txt"
attempts = 0
Passwords = []

with open(wordlist, 'r') as wordlist:
    for line in wordlist:
        passwd = line.strip('\n')
        Passwords.append(passwd)
    wordlist.close()
# ----------------------------------------------------------


def Cracker(PasswList):
    global attempts
    for z in reversed(range(101)):
        Crypted = True
        while Crypted:
            try:
                with ZipFile(str(z) +".zip", 'r') as zipObj:
                    zipObj.extractall(pwd=str.encode(PasswList[attempts]))
                print(f"[!] {z}.zip Unzipped - Password : {PasswList[attempts]} - Attempts: {attempts}")
                Crypted = False
                attempts = 0
            except Exception:
                attempts += 1
                print(f"[X] {z}.zip Unzip Failed - Tried Password : {PasswList[attempts]} - Attempts: {attempts} ")
                continue


Cracker(Passwords)