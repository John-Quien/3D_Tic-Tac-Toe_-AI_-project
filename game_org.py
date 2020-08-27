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
    gameEnd = 0
    while gameWin() != True or gameEnd == 64:
        playerTurn = False
        if player = 1:
            print("Player 1: Enter the number in brackets to select cube position")
        if player = -1:
            print("Player 2: Enter the number in brackets to select cube position")
        while playerTurn == False:
            layer = eval(input("Layer select : Front Layer (0), Front Middle Layer (1), Back Middle Layer (2), Back Layer (3)"))
            row = eval(input("Row select : Top Row (0), Top Middle Row (1), Bottom Middle Row (2), Bottom Row (3)"))
            cube = eval(input("Cube select: Left (0), Middle Left (1), Middle Right (2), Right (3)"))
            if gameCube[layer,row,cube] == 0:
                gameCube[layer,row,cube] = player
                playerTurn == True
                gameEnd += 1
                player = -player
                print("Successful Placement: Current Gameboard", gameCube)
            else:
                print("There is already a placement there! Please choose another spot on the gameboard.")
                playerTurn == False

def gameWin():



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
