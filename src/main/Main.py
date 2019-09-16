import os
from pynput.keyboard import Key, Listener

from src.main.SQLConnector import accessDB
from src.main.SQLConnector import checkUser
from src.main.SQLConnector import showVisibileTables
from src.main.SQLConnector import showEditableTables
from pip._vendor.distlib.compat import raw_input


"""
Classe principale del sistema, fornisce i menu di avvio
"""

roles = ['CEO', 'HR', 'SUPERVISORS', 'CONSULTANT']
azioniConcesse=['visualizza dati', 'modifica dati']

class Menu:

    def __init__(self, newArray, msg, flag):
        self.array = newArray
        self.selected = 0
        self.flag = flag
        self.message = msg
        self.choice = 0
        self.done = False

    def setArray(self,myArray):
        global array
        for index in range(0, len(myArray)):
            array.append(myArray[index])


    def show_menu(self):
        clear = "\n" * 100
        print (clear)
        print(self.message)
        if self.flag == True:
            for i in range(0, len(self.array)):
                print("{1} {0}. ".format(i, ">" if self.selected == i else " ", "<" if self.selected == i else " "), self.array[i])
        else:
            for i in range(0, len(self.array)):
                print("{0}. ".format(i), self.array[i])

    def on_press(self, key):
        if key == Key.down:
            if self.selected == len(self.array):
                self.selected = -1
                self.show_menu()
            self.selected += 1
            self.show_menu()
        elif key == Key.up:
            if self.selected == -1:
                self.selected = len(self.array)
                self.show_menu()
            self.selected -= 1
            self.show_menu()
        else:
            pass

    def on_release(self, key):
        if key == Key.enter:
            self.choice = self.selected
            return False
        

def mainMenu():
    global roles
    myMenu = Menu(roles, 'Accedi con il tuo ruolo, premi "invio" per scegliere:', True)

    myMenu.show_menu()

    with Listener(
            on_press=myMenu.on_press,
            on_release=myMenu.on_release) as listener:
        listener.join()

    roleNumber = myMenu.selected
    print('Hai scelto il ruolo: ', myMenu.array[myMenu.selected])


    print('***********************')
    return roles[myMenu.selected], roleNumber

def actionMenu(

):
    global azioniConcesse
    menuAzioni = Menu(azioniConcesse, 'Queste sono le azioni concesse, inserisci il numero per scegliere: ', False)

    menuAzioni.show_menu()


    choice = int(raw_input("scelta: "))

    return choice



def main():

    #mostra il menu iniziale, dove propone i ruoli
    roleUsed, roleNumber = mainMenu()

    print ('inserisci le credenziali per il ruolo ',roleUsed,":")

    nomeUtente = str(raw_input("usename: "))
    matricola = int(raw_input('matricola: '))
    secretKey = str(raw_input('chiave segreta: '))

    cur = accessDB()

    result = checkUser(roleUsed, nomeUtente, matricola, secretKey, cur)

    if (result == True):
        actionChoose = actionMenu()
        if actionChoose == 0:
            print('\nhai deciso di visualizzare i dati, queste sono le tabelle che puoi consultare:')
            showVisibileTables(roleNumber, cur, roles)
        else:
            print('hai deciso di inserire nuovi  dati!\n')
            print('***********************')
            showEditableTables(roleNumber,cur, roles)

    else:
        print ('esecuzione interrotta .....')




if __name__ == '__main__':
    main()
