"""
Questa classe contiene il metodo utilizzato per cercare il valore della
key utilizzata nella cifratura di ElGamal
"""

import random

"""
Questo metodo valuta se a e b sono relativamente primi tra loro.
"""
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

"""
Metodo per generare un k tale che gcd(k, numero primo scelto) sia primo;
ovvero k e il numero primo scelto devono essere relativamente primi
"""
def gen_key(q):
    key = random.randint(1, q)
    while gcd(q, key) != 1:
        key = random.randint(1, q)

    print ("la key vale: ",key)
    return key

def main():
    primeNumber = int(input('inserisci il tuo numero primo: '))

    key = gen_key(primeNumber)

    print ('la key trovata è: ', key)


if __name__ == '__main__':
    main()
