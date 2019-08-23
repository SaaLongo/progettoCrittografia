
# i numeri primi devono necessariamente essere composti di almeno 8 bit: questo
# è necessario al fine di poter cifrare anche le stringhe
numeroPrimoCEO = 4549

# generatore trovato tramite il modulo "findGenerators.py"
generatoreCEO = 6

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

def getPrimeNumberCEO():
    return numeroPrimoCEO

def getGeneratorCEO():
    return generatoreCEO
"""
Questo metodo genera il valore alfa (la chiave privata) 
"""
def generatePrivateKey(nomeUtente, matricola, secretKey):
    intUser = int(nomeUtente)
    alfaValue = (intUser * matricola * secretKey) % numeroPrimoCEO

    return alfaValue

"""
questo metodo si occupa dell'encryption dopo aver richiesto
le credenziali al CEO
"""
def encrypt(nome, matricola, secretKey):
    return True