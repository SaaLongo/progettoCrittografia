import MySQLdb

from src.main.SQLConnector import accessDB
from src.main.CEOChiper import generateGammaValue
from src.main.CEOChiper import encryptCEO
from src.main.ElGamal import getKey

def concatenate(en_msg, p):
    string = "'{0}///{1}'".format(en_msg,p)
    return string

def convertTuple(tuple):
    str =  ','.join(tuple)
    return str

def encryptCEOTable():
    cursor = accessDB()
    query = "select * from ceo;"
    cursor.execute(query)
    row = cursor.fetchall()

    #prendo la key
    key = getKey()

    if (len(row) != 0):
        username = str(row[0][2]).strip()
        matricola = str(row[0][3]).strip()
        secretKey = str(row[0][4]).strip()

        print (username)

        gammaV = generateGammaValue(username,matricola,secretKey)

        tuple = [0]*len(row[0])

        for index in range(0, len(tuple)):
            plaintext = str(row[0][index])
            en_msg, p = encryptCEO(plaintext,key, gammaV)
            tuple[index] = concatenate(en_msg, p)

        #rimuovo la vecchia tupla
        q = "delete from ceo where matricola={0};".format(matricola)

        cursor.execute(q)

        #inserisco tupla cifrata

        myq = "insert into ceo(cognome, nome, username, matricola, secretKey) values("
        myq+=convertTuple(tuple)
        myq+=");"

        print (myq)
        cursor.execute(myq)

    else:
        print ("no tuple found!")




def main():
    encryptCEOTable()


if __name__ == '__main__':
    main()