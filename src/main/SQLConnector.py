from MySQLdb import connect
from MySQLdb import Error
from pip._vendor.distlib.compat import raw_input
from src.main.CEOChiper import generateGammaValue
from src.main.CEOChiper import encryptCEO
from src.main.ElGamal import key

from prettytable import PrettyTable

def encryptCEORow(nomeUtente, matricola, secretKey, cur):
    #il CEO è sempre uno, quindi la query sarà fatta direttamente in questo metodo

    query = "select * from ceo;"
    cur.execute(query)
    row = cur.fetchall()

    gammaValue = generateGammaValue(nomeUtente, matricola, secretKey)

    #cancello la tupla del ceo
    query = "delete from ceo where matricola = {0}".format(row[0][3])
    cur.execute(query)

    #cripto tutti i valori e li inserisco in un vettore
    en_values = []
    for index in range (len(row)):
        en_msg, p = encryptCEO(row[index], key, gammaValue)
        string = "{0} /// {1}".format(en_msg,p)
        en_values[index] = string

    query = "insert into ceo(cognome, nome, username, matricola, secretKey) values ("
    for l in range(len(en_values)):
        query += "'"
        query += en_values[l]
        query += "'"
        if index == len(en_values) - 1:
            query += ","
    cur.execute(query)




def encryptDB(row, cur):
    nomeUtente = str(input('nomeUtente: '))
    matricola = int(input('matricola: '))
    secretKey = str(input('chiave segreta: '))


    encryptCEORow(nomeUtente, matricola, secretKey,  cur)

def main():
    cur = accessDB()
    query = "select * from ceo"
    cur.execute(query)
    row = cur.fetchall()
    for index in range(0, len(row)):
        print (row[index])
        encryptDB(row, cur)

    query = "select * from ceo"
    cur.execute(query)
    row = cur.fetchall()
    for index in range(0, len(row)):
        print (row[index])


def accessDB():
    try:
        db = connect(host="localhost",
                     user="root",
                     passwd="password",
                     database="progettoCritto")  # name of the data base

        # il cursore permette di eseguire le query
        cur = db.cursor()

        return cur

    except Error as e:
        print("Error reading data from MySQL table", e)



def checkUser(role, username, matricola, secretKey, cur):
    query = "select * from "
    query += role
    query += " where matricola="
    query+=str(matricola)
    cur.execute(query)
    row = cur.fetchall()
    if (len(row) == 0):
        #se non ci sono corrispondenze per la matricola
        print ('nessuna corrispondenza nel database, le credenziali inserite non sono valide')
        return False
    else:
        print ('corrispondenza trovata! verifico le altre credenziali...')
        if (row[0][3] == matricola):
            if (row[0][2] == username):
                if (row[0][4] == secretKey):
                    print('verifica completata, adesso puoi accedere, ', row[0][1], '!')
                    return True
                else:
                    print ('secret key errata! Riprova')
                    return False

            else:
                print ('nome utente non valido! Riprova')
                return False
        else:
            return False

def showVisibileTables(roleNumber, cursor, roles):

    for index in range(roleNumber,len(roles)):
        query = "select * from "
        query += roles[index]
        cursor.execute(query)
        row = cursor.fetchall()


        #recuepero i nomi delle colonne
        queryCol = "show columns from "
        queryCol += roles[index]
        cursor.execute(queryCol)
        colNames = cursor.fetchall()

        print('\ntabella {0}: '.format(roles[index]))

        if (len(row) == 0):
            print('tabella {0} vuota'.format(roles[index]))
        else:
            attributes = []
            for l in range(0, len(colNames)):
                attributes.append(colNames[l][0])

            table = PrettyTable(attributes)
            #TODO quando ci sarà il key manager è necessario filtrare le tuple mostrate
            for i in range (0, len(row)):
                table.add_row(row[i])

            print (table)
        print('\n***********************')


def showEditableTables(roleNumber, cursor, roles):

    print ('puoi modificare le seguenti tabelle: ')

    if roleNumber == len(roles) + 1:
        print ('tabella CONSULTANT, ecco la struttura:')

        #recuepero i nomi delle colonne
        queryCol = "show columns from CONSULTANT"
        cursor.execute(queryCol)
        colNames = cursor.fetchall()

        attributes = []
        for l in range(0, len(colNames)):
            attributes.append(colNames[l][0])

        table = PrettyTable(attributes)
        print (table)

    for index in range(roleNumber+1, len(roles)):
        print ('tabella {0}, ecco la struttura: \n'.format(roles[index]))

        # recuepero i nomi delle colonne
        queryCol = "show columns from "
        queryCol += roles[index]
        cursor.execute(queryCol)
        colNames = cursor.fetchall()

        attributes = []
        for l in range(0, len(colNames)):
            attributes.append(colNames[l][0])

        table = PrettyTable(attributes)
        print(table)
        print('\n***********************')

def editTable(role, cursor):
    # recuepero i nomi delle colonne
    queryCol = "show columns from "
    queryCol += role
    cursor.execute(queryCol)
    colNames = cursor.fetchall()

    attributes = []
    for l in range(0, len(colNames)):
        attributes.append(colNames[l][0])

    values = []

    print('\n***********************')
    print ('stai modificando la tabella {0} inserisci i valori della nuova tupla\n'.format(role))

    #raccolta dei valori da inserire
    for i in range(0, len(attributes)):
        val = raw_input('{0}: '.format(attributes[i]))
        values.append(val)

    #creazione della prima parte della stringa query
    insertion = 'insert into {0} ('.format(role)
    for index in range(0, len(attributes)):
        insertion+= attributes[index]
        if index != len(attributes)-1:
            insertion += ', '
    insertion += ') values ('

    #inserimento dei valori nella query
    for t in range(0, len(values)):
        insertion += "'"
        insertion+= values[t]
        insertion += "'"
        if t != len(values)-1:
            insertion += ', '

    insertion += ') '

    print (insertion)

    cursor.execute(insertion)


def fetchCredentials(username, role, targetRole):
    pass

if __name__ == '__main__':
    main()