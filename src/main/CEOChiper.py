from src.main.ElGamal import encrypt
from src.main.ElGamal import decrypt
from src.main.ElGamal import gen_key
from src.main.ElGamal import power

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
una tipla che rappresenta la chiave pubblica, composta da:
- numero primo usato
- generatore scelto 
- betaValue = generatore elevato al valore della key
"""
def generatePublicKey():
    publicKey = []
    publicKey.append(numeroPrimoCEO)
    publicKey.append(generatoreCEO)
    key = gen_key(publicKey[0])
    betaValue = pow(generatoreCEO,key) % numeroPrimoCEO
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
def generateGammaValue(nomeUtente, matricola, secretKey):
    intUser = stringToNumbers(nomeUtente)
    secretKey =  stringToNumbers(secretKey)
    gammaValue = (intUser * matricola * secretKey) % numeroPrimoCEO

    print ('gammaValue: ', gammaValue)
    return gammaValue

"""
questo metodo si occupa dell'encryption dopo aver richiesto
le credenziali al CEO
@:param publicKey = chiave pubblica del CEO
        plaintext = testo in chiaro da cifrare
"""
def encryptCEO(publicKey, plaintext, key, gammaValue):
    primeNumber = getPrimeNumberCEO()
    generator = getGeneratorCEO()
    betaValue = power(generator, key, primeNumber)

    en_msg, p = encrypt(plaintext, primeNumber, betaValue, generator,gammaValue, key)


    return en_msg,p

def decryptCEO(publicKey, en_msg, p, gammaValue, key):
    # q = primeNumber
    q = publicKey[0]
    dr_msg = decrypt(en_msg, p, key, q, gammaValue)

    return dr_msg

def main():

    nomeUtente = str(input('nomeUtente: '))
    matricola = int(input('matricola: '))
    secretKey = str(input('chiave segreta: '))

    publicKey = generatePublicKey()

    gammaValue = generateGammaValue(nomeUtente,matricola,secretKey)
    msg = 'Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa.'
    print ("messaggio in chiaro:", msg)
    key = gen_key(publicKey[0])
    en_msg, p = encryptCEO(publicKey,msg, key,gammaValue)

    dr_msg = decryptCEO(publicKey,en_msg, p, gammaValue, key)
    dmsg = ''.join(dr_msg)
    print("Messaggio decifrato :", dmsg);


if __name__ == '__main__':
    main()
