from MySQLdb import connect
from MySQLdb import Error

def encryptDB():
    pass

def accessDB():
    try:
        db = connect(host="localhost",
                     user="root",
                     passwd="password",
                     database="progettoCritto")  # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
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


def insertInfo(query):
    pass

def executeQuery(query):
    pass

def fetchCredentials(username, role, targetRole):
    pass
