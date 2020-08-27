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
    winCondition = False
    while winCondition != True or gameEnd == 64:
        playerTurn = False
        if player == 1:
            print("Player 1: Enter the number in brackets to select cube position")
        if player == -1:
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
                winCondition = gameWin(gameCube)
            else:
                print("There is already a placement there! Please choose another spot on the gameboard.")
           

def gameWin(gameCube):
    gameCube1D = np.array([gameCube[0, 0, 0], gameCube[0, 0, 1], gameCube[0, 0, 2], gameCube[0, 0, 3],
                             gameCube[0, 1, 0], gameCube[0, 1, 1], gameCube[0, 1, 2], gameCube[0, 1, 3],
                             gameCube[0, 2, 0], gameCube[0, 2, 1], gameCube[0, 2, 2], gameCube[0, 2, 3],
                             gameCube[0, 3, 0], gameCube[0, 3, 1], gameCube[0, 3, 2], gameCube[0, 3, 3],

                             gameCube[1, 0, 0], gameCube[1, 0, 1], gameCube[1, 0, 2], gameCube[1, 0, 3],
                             gameCube[1, 1, 0], gameCube[1, 1, 1], gameCube[1, 1, 2], gameCube[1, 1, 3],
                             gameCube[1, 2, 0], gameCube[1, 2, 1], gameCube[1, 2, 2], gameCube[1, 2, 3],
                             gameCube[1, 3, 0], gameCube[1, 3, 1], gameCube[1, 3, 2], gameCube[1, 3, 3],

                             gameCube[2, 0, 0], gameCube[2, 0, 1], gameCube[2, 0, 2], gameCube[2, 0, 3],
                             gameCube[2, 1, 0], gameCube[2, 1, 1], gameCube[2, 1, 2], gameCube[2, 1, 3],
                             gameCube[2, 2, 0], gameCube[2, 2, 1], gameCube[2, 2, 2], gameCube[2, 2, 3],
                             gameCube[2, 3, 0], gameCube[2, 3, 1], gameCube[2, 3, 2], gameCube[2, 3, 3],

                             gameCube[3, 0, 0], gameCube[3, 0, 1], gameCube[3, 0, 2], gameCube[3, 0, 3],
                             gameCube[3, 1, 0], gameCube[3, 1, 1], gameCube[3, 1, 2], gameCube[3, 1, 3],
                             gameCube[3, 2, 0], gameCube[3, 2, 1], gameCube[3, 2, 2], gameCube[3, 2, 3],
                             gameCube[3, 3, 0], gameCube[3, 3, 1], gameCube[3, 3, 2],
                             gameCube[3, 3, 3]])
    for i in range(0,4):
        win = gameCube1D[0+(i*4)]+gameCube1D[1+(i*4)]+gameCube1D[2+(i*4)]+gameCube1D[3+(i*4)] #horizontal layer wins
        if win == 4 or win == -4
            return True
        win = gameCube1D[0+(i*4)]+gameCube1D[17+(i*4)]+gameCube1D[34+j+(i*4)]+gameCube1D[51+(i*4)] #-slope horizontal depth wins
        if win == 4 or win == -4
            return True
    for i in range(0,4): #
        for j in range(0,4):
            win = gameCube1D[0+j+(i*16)]+gameCube1D[4+j+(i*16)]+gameCube1D[8+j+(i*16)]+gameCube1D[12+j+(i*16)] #vertical layer wins
            if win == 4 or win== -4:
                return True
            win = gameCube1D[0+j+(i*4)]+gameCube1D[16+j+(i*4)]+gameCube1D[32+j+(i*4)]+gameCube1D[48+j+(i*4)] #depth wins
            if win == 4 or win == -4:
                return True

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
