"""
Classe principale del sistema, fornisce i menu di avvio
"""
import os

import pygame

roles = ['CEO', 'HR', 'SUPERVISOR', 'CONSULTANT']


def mainMenu(posArrow):
    for index in range(0, len(roles)):
        if (posArrow == index):
            print("> ", roles[index])
        else:
            print("  ", roles[index])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if posArrow == (len(roles) - 1):
                    posArrow = 0
                    mainMenu(posArrow)
                else:
                    posArrow = posArrow + 1
                    mainMenu(posArrow)
                    os.system('cls')

            elif event.type == pygame.KEYUP:
                if posArrow == 0:
                    posArrow = len(roles) - 1
                    mainMenu(posArrow)
                else:
                    posArrow = posArrow - 1
                    mainMenu(posArrow)


def main():
    posArrow = 0
    pygame.init()
    mainMenu(posArrow)


if __name__ == '__main__':
    main()
