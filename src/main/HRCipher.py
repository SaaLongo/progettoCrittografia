from src.main.ElGamal import encrypt
from src.main.ElGamal import decrypt
from src.main.ElGamal import power
from src.main.ElGamal import q
from src.main.ElGamal import g
from src.main.ElGamal import key

# questo valore è utilizzato nel momento in cui si trasformano
# gli attributi di un ceo in un numero
deltaHR = 56

"""
Questo metodo è utile per trasformare le lettere in numeri, entra in gioco
quando si produce il gammaValue
"""
def stringToNumbers(string):
    outputValue = []
    finalValue = 1
    for character in string:
        number = ord(character) - deltaHR
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
    gammaValue = (intUser * matricola * secretKey) % q

    print ('gammaValue: ', gammaValue)
    return gammaValue

"""
questo metodo si occupa dell'encryption dopo aver richiesto
le credenziali al CEO
@:param publicKey = chiave pubblica del CEO
        plaintext = testo in chiaro da cifrare
"""
def encryptHR(plaintext, key, gammaValue):
    betaValue = power(g, key, q)
    en_msg, p = encrypt(plaintext, betaValue, gammaValue, key)

    return en_msg,p

def decryptHR(en_msg, p, gammaValue, key):
    dr_msg = decrypt(en_msg, p, key,gammaValue)

    return dr_msg

def main():

    nomeUtente = str(input('nomeUtente: '))
    matricola = int(input('matricola: '))
    secretKey = str(input('chiave segreta: '))

    gammaValue = generateGammaValue(nomeUtente,matricola,secretKey)
    msg = 'Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa.'
    print ("messaggio in chiaro:", msg)
    en_msg, p = encryptHR(msg, key,gammaValue)

    dr_msg = decryptHR(en_msg, p, gammaValue, key)
    dmsg = ''.join(dr_msg)
    print("Messaggio decifrato :", dmsg);


if __name__ == '__main__':
    main()
