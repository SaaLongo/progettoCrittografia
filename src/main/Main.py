"""
Classe principale del sistema, fornisce i menu di avvio
"""
import keyboard
from src.main.Menu import Menu

roles = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']


def mainMenu():
    global roles
    print('menu principale, premi spazio per scegliere:\n')
    myMenu = Menu(roles)

    myMenu.show_menu()
    keyboard.add_hotkey('up', myMenu.up)
    keyboard.add_hotkey('down', myMenu.down)
    keyboard.add_hotkey('a', lambda: myMenu.enter())

    keyboard.wait('a', lambda: myMenu.enter())

    print('selection is: ', myMenu.selected)


def main():

    #mostra il menu iniziale, dove propone i ruoli
    mainMenu()


if __name__ == '__main__':
    main()
