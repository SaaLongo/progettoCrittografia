import os
from pynput.keyboard import Key, Listener

import SQLConnector
from pip._vendor.distlib.compat import raw_input


"""
Classe principale del sistema, fornisce i menu di avvio
"""

roles = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']
azioniConcesse=['Inserisci utente', 'visualizza dati', 'modifica dati']

class Menu:

    def __init__(self, newArray, msg):
        self.array = newArray
        self.selected = 0
        self.iterate = True
        self.message = msg
        self.choice = 0
        self.done = False

    def setArray(self,myArray):
        global array
        for index in range(0, len(myArray)):
            array.append(myArray[index])


    def show_menu(self):
        os.system('clear')
        print(self.message)
        for i in range(0, len(self.array)):
            print("{1} {0}. ".format(i, ">" if self.selected == i else " ", "<" if self.selected == i else " "), self.array[i])

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
    print('MENU PRINCIPALE...\n')
    myArray = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']
    myMenu = Menu(myArray, 'premi e per scegliere:')

    myMenu.show_menu()
    # Collect events until released

    with Listener(
            on_press=myMenu.on_press,
            on_release=myMenu.on_release) as listener:
        listener.join()

    print('Hai scelto: ', myMenu.array[myMenu.selected])


    print('***********************')
    return roles[myMenu.selected]


def main():

    #mostra il menu iniziale, dove propone i ruoli
    roleUsed = mainMenu()

    print ('inserisci le credenziali per il ruolo ',roleUsed," :")

    nomeUtente = str(raw_input("nomeUtente: "))
    matricola = int(raw_input('matricola: '))
    secretKey = str(raw_input('chiave segreta: '))

    #cur = accessDB()

    #result = checkUser(roleUsed, nomeUtente, matricola, secretKey, cur)

    result = True
    if result == True:
        print("success")
    else:
        print("defeat")


if __name__ == '__main__':
    main()
