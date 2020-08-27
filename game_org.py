## 4x4x4  3D  TicTacToe ##
import time
import random
import numpy as np
def gameRules():
    print("Insert Rules")

def gameStart():
    print("Game Start!")
    print("Who will make the first move?")
    # -1 is player 2, 1 is player 1
    playerFirst = eval(input("Player 1: Enter 1 | Player 2: Enter 2 | Random: Enter 3"))
    if playerFirst == 3:
        playerOption = random.choice([-1,1])
        if playerOption == -1:
            print("Player 2 goes first!")
            game(playerOption)
        else:
            print("Player 1 goes first!")
            game(playerOption)

    if playerFirst == 2:
        playerOption = -1
        print("Player 2 goes first!")
        game(playerOption)
    else:
        playerOption = 1
        print("Player 1 goes first!")
        game(playerOption)

def game(player):
    gameCube = np.zeros((4, 4, 4))
    while (gameWin() or gameEnd()) != True:
        #stuff

gameWin()

def gameEnd():




def exitGame():
    print("Thanks for playing! We hope you come again ~ ")
    time.sleep(2.5)
    exit()

print("Hello! Welcome to 3D 4x4x4 TicTacToe!")
menuPage = eval(input("For Rules: Enter 1 | To Play: Enter 2 | To Exit: Enter 3"))
if menuPage == 1:
    gameRules()
    menuPage = eval(input("To Play: Enter 2 | To Exit: Enter 3"))
if menuPage == 2:
    gameStart()
if menuPage == 3:
    exitGame()