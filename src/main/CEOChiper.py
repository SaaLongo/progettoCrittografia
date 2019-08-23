from src.main.ElGamal import encrypt
from src.main.ElGamal import decrypt

# i numeri primi devono necessariamente essere composti di almeno 8 bit: questo
# è necessario al fine di poter cifrare anche le stringhe
numeroPrimoCEO = 4549

# generatore trovato tramite il modulo "findGenerators.py"
generatoreCEO = 6

def getPrimeNumberCEO():
    return numeroPrimoCEO

def getGeneratorCEO():
    return generatoreCEO

"""
Questo metodo genera la public key del CEO, come prevede El Gamal produce
una tipla che rappresenta la chiave pubblica
"""
def generatePublicKey(privateKey):
    publicKey = []
    publicKey.append(numeroPrimoCEO)
    publicKey.append(generatoreCEO)
    betaValue = pow(generatoreCEO,privateKey) % numeroPrimoCEO
    publicKey.append(betaValue)

    return publicKey

def stringToNumbers(string):
    outputValue = []
    finalValue = 1
    for character in string:
        number = ord(character) - 96
        outputValue.append(number)

    for index in range (1,len(outputValue)-1):
        finalValue = outputValue[index] * finalValue

    print (finalValue)
    return finalValue

"""
Questo metodo genera il valore alfa (la chiave privata) 
"""
def generatePrivateKey(nomeUtente, matricola, secretKey):
    intUser = stringToNumbers(nomeUtente)
    secretKey =  stringToNumbers(secretKey)
    alfaValue = (intUser * matricola * secretKey) % numeroPrimoCEO

    print ('alfavalue: ', alfaValue)
    return alfaValue

"""
questo metodo si occupa dell'encryption dopo aver richiesto
le credenziali al CEO
@:param publicKey = chiave pubblica del CEO
        plaintext = testo in chiaro da cifrare
"""
def encryptCEO(publicKey, plaintext, alfaValue):
    primeNumber = getPrimeNumberCEO()
    generator = getGeneratorCEO()
    betaValue = publicKey[2]

    en_msg, p = encrypt(plaintext, primeNumber, betaValue, generator, alfaValue)


    return en_msg,p

def decryptCEO(publicKey, en_msg, p, privateKey):
    q = getPrimeNumberCEO()
    dr_msg = decrypt(en_msg, p, privateKey, q)

    return dr_msg

def main():

    nomeUtente = str(input())
    matricola = int(input())
    secretKey = str(input())

    privateKey = generatePrivateKey(nomeUtente, matricola, secretKey)
    publicKey = generatePublicKey(privateKey)

    msg = 'ciao'
    en_msg, p = encryptCEO(publicKey,msg, privateKey)

    dr_msg = decryptCEO(publicKey,en_msg, p, privateKey)
    dmsg = ''.join(dr_msg)
    print("Messaggio decifrato :", dmsg);


if __name__ == '__main__':
    main()
