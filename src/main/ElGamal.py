import random
#from src.main.CEOChiper import getGeneratorCEO
#from src.main.CEOChiper import getPrimeNumberCEO


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


def gen_key(q,alfaValue):
    key = random.randint(1, q)
    while gcd(q, key) != 1:
        key = random.randint(alfaValue, q)

    return key


"""
Metodo di esponenziazione modulare
"""


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)

    return x % c


"""
Algoritmo di ElGamal di cifratura asimmetrica
@:param msg: plaintext da cifrare
        q = numero primo scelto 
        h = betaValue, valore di Beta dato dal pow(generatore, alfa)
        g = generatore utilizzato
@:return en_msg = array del messaggio cifrato
         p = generatore elevato alla k mod q
"""


def encrypt(msg, q, h, g,alfaValue):
    en_msg = []

    k = gen_key(q,alfaValue)  # Private key for sender
    betaValue = power(g, k, q)
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    print('messaggio cifrato: ', en_msg)

    return en_msg, p

"""
Algoritmo di ElGamal di decifratura asimmetrica
@:param en_msg: ciphertext da decifrare
        q = numero primo scelto 
        p = generatore elevato alla k mod q
        key = k scelto
@:return dr_msg = array del messaggio decifrato

"""

def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg

""""
Funzione di main generata per il testing
"""
def main():
    msg = 'encryption'
    print("Messaggio originale :", msg)

    #primeNumber = getPrimeNumberCEO()
    #generator = getGeneratorCEO()
    primeNumber = 0
    generator = 0

    # valore k privato
    key = gen_key(primeNumber)
    betaValue = power(generator, key, primeNumber)
    print('numero primo usato: ',primeNumber)
    print("generatore usato : ", generator)
    print("g^a vale : ", betaValue)

    en_msg, p = encrypt(msg, primeNumber, betaValue, generator)
    dr_msg = decrypt(en_msg, p, key, primeNumber)
    dmsg = ''.join(dr_msg)
    print("Messaggio decifrato :", dmsg);


if __name__ == '__main__':
    main()
