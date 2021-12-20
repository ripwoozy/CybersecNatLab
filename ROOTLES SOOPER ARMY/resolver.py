# SERVER LINUX --> nc rsa.challs.olicyber.it 10300

# ESPONENTE PRIVATO "d" DA CALCOLARE SUL SITO SEGUENTE
# LINK --> https://www.dcode.fr/modular-inverse

from Crypto.Util.number import bytes_to_long 

def rsa_init(p,q):
    fin = (p -1)*(q-1)
    print (fin)
    print("\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def encrypt(m,n):
    s = bytes_to_long(str.encode(m))
    c = pow(s, 65537, n)
    print (c)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def main():
    p = int(input("First Prime Number:     "))
    q = int(input("Second Prime Number:     "))
    n = p*q
    print (n)
    rsa_init(p,q)
    m = input("Text to Encrypt:    ")
    encrypt(m,n)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

main()
