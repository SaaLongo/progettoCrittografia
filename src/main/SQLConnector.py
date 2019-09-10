import MySQLdb
from MySQLdb import Error

def encryptDB():
    pass

def accessDB():
    try:
        db = MySQLdb.connect(host="localhost",
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
    query = "select * from "+role+" where matricola = "+matricola
    cur.execute(query)
    row = cur.fetchall()
    if (len(row) == 0):
        #se non ci sono corrispondenze
        print ('nessuna corrispondenza nel database')
        return False
    else:
        print ('corrispondenza trovata! verifico le altre credenziali')
        if (row[3] == matricola and row[2]==username and row[4]==secretKey):
            print('verifica completata, adesso puoi accedere, ', row[1])
            return True
        else:
            print('verifica completata, alcune informazioni non sono correte. Riprova')
            return False



def insertInfo(query):
    pass

def deleteInfo(query):
    pass

def executeQuery(query):
    pass

def fetchCredentials(username, role, targetRole):
    pass
    ##questa funzione deve permettere ad un utente di livello più alto
    ## di leggere le info alle tabelle di livello più basso, recuperando le credenziali ai livelli più
    ##bassi