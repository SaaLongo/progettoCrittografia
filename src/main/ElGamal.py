

# i numeri primi devono necessariamente essere composti di almeno 8 bit: questo
# è necessario al fine di poter cifrare anche le stringhe, si farà uso dello
# stesso numero primo per tutti i cifrari, cambierà solamente il gammaValue
q = 4549

# generatore trovato tramite il modulo "findGenerators.py"
g = 6


# il valore della key rappresenta la chiave privata, in tal caso la chiave privata
# sarà unica per tutti gli utenti, l'obiettivo di questa soluzione è quello di
# sfruttare la sicurezza e le performance dei cifrari asimmetrici associandolo
# alla versatilità di quelli simmetrici. L'ABE sarà realizzata attraverso l'uso
# del gammaValue
key = 798


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


def encrypt(msg, h, gammaValue,k):
    en_msg = []

    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = (s * ord(en_msg[i])) + gammaValue

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

def decrypt(en_msg, p, key, gammaValue):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int((en_msg[i]-gammaValue) / h)))

    return dr_msg

""""
Funzione di main generata per il testing
"""
def main():
    msg = 'encryption'
    print("Messaggio originale :", msg)


    betaValue = power(g, key, q)
    gammaValue = 100
    print('numero primo usato: ',q)
    print("generatore usato : ", g)
    print("g^a vale : ", betaValue)

    en_msg, p = encrypt(msg, betaValue, gammaValue,key)
    dr_msg = decrypt(en_msg, p, key, gammaValue)
    dmsg = ''.join(dr_msg)
    print("Messaggio decifrato :", dmsg);


if __name__ == '__main__':
    main()
