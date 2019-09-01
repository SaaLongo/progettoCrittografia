import os

import keyboard

class Menu:

    def __init__(self, newArray, msg):
        self.array = newArray
        self.selected = 0
        self.iterate = True
        self.message = msg

    def setArray(self,myArray):
        global array
        for index in range(0, len(myArray)):
            array.append(myArray[index])


    def show_menu(self):
        os.system('clear')
        print(self.message)
        for i in range(0, len(self.array)):
            print("{1} {0}. ".format(i, ">" if self.selected == i else " ", "<" if self.selected == i else " "), self.array[i])

    def up(self):
        if self.selected == 0:
            self.selected = len(self.array)
            self.show_menu()
        self.selected -= 1
        self.show_menu()

    def down(self):
        if self.selected == len(self.array):
            self.selected = -1
            self.show_menu()
        self.selected += 1
        self.show_menu()


"""
main di testing
"""
def main():
    myArray = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']
    myMenu = Menu(myArray)

    myMenu.show_menu()
    keyboard.add_hotkey('up', myMenu.up)
    keyboard.add_hotkey('down', myMenu.down)
    keyboard.add_hotkey('e', myMenu.enter())

    keyboard.wait('e', lambda: myMenu.enter())
    keyboard.wait('E', lambda: myMenu.enter())


    print ('Hai scelto: ', myMenu.array[myMenu.selected - 1])



if __name__ == '__main__':
    main()