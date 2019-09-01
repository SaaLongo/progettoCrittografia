"""
Classe principale del sistema, fornisce i menu di avvio
"""
import keyboard

import MenuClass

roles = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']


def mainMenu():
    global roles
    print('menu principale, premi spazio per scegliere:\n')
    myMenu = MenuClass.Menu(roles,'premi \'e\' per scegliere il ruolo d\'accesso: ')

    myMenu.show_menu()
    keyboard.add_hotkey('up', myMenu.up)
    keyboard.add_hotkey('down', myMenu.down)

    keyboard.wait('e')
    #TODO: close keyboard stream
    print('Hai scelto: ', roles[myMenu.selected-1])
    return roles[myMenu.selected - 1]


def main():

    #mostra il menu iniziale, dove propone i ruoli
    mainMenu()

    print ('inserisci le credenziali per il ruolo scelto.')

    nomeUtente = str(input('nomeUtente: '))
    matricola = int(input('matricola: '))
    secretKey = str(input('chiave segreta: '))





if __name__ == '__main__':
    main()
