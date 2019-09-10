"""
Classe principale del sistema, fornisce i menu di avvio
"""
import keyboard

import MenuClass
from src.main.SQLConnector import checkUser
from src.main.SQLConnector import accessDB
from pip._vendor.distlib.compat import raw_input



roles = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']
azioniConcesse=['Inserisci utente', 'visualizza dati', 'modifica dati']


def mainMenu():
    global roles
    print('menu principale, premi spazio per scegliere:\n')
    myMenu = MenuClass.Menu(roles,'premi \'e\' per scegliere il ruolo d\'accesso: ')

    myMenu.show_menu()
    keyboard.add_hotkey('up', myMenu.up)
    keyboard.add_hotkey('down', myMenu.down)

    keyboard.wait('e')
    keyboard.remove_all_hotkeys()
    keyboard.press('delete')

    print('Hai scelto: ', roles[myMenu.selected])
    print('***********************')
    return roles[myMenu.selected]


def main():


    #keyboard.add_hotkey('ctl'+'c', encryptDB())
    #mostra il menu iniziale, dove propone i ruoli
    roleUsed = mainMenu()

    print ('inserisci le credenziali per il ruolo ',roleUsed," :")

    nomeUtente = str(raw_input("nomeUtente: "))
    matricola = int(raw_input('matricola: '))
    secretKey = str(raw_input('chiave segreta: '))

    cur = accessDB()

    checkUser(roleUsed, nomeUtente, matricola, secretKey, cur)








if __name__ == '__main__':
    main()
