import sqlite3

def checkUser(role, username, matricola, secretKey):
    pass

def insertInfo(query):
    pass

def deleteInfo(query):
    pass
    ##questa funzione deve permettere di cancellare dei record
    ## solo se l'utente può leggere in quella tabella

def executeQuery(query):
    pass

def fetchCredentials(username, role, targetRole):
    pass
    ##questa funzione deve permettere ad un utente di livello più alto
    ## di leggere le info alle tabelle di livello più basso, recuperando le credenziali ai livelli più
    ##bassi