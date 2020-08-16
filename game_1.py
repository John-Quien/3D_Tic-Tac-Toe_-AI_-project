import numpy as np
import logging

class Game:
    def __init__(self):
        self.currentPlayer = 1
        self.gameState = GameState(np.zeros(4,4,4))
        self.actionSpace = np.zeros(4,4,4)
        self.pieces = {'1':'X','0':'-','-1':'0'} #dictionary, mapping word to definition
        self.cube_shape = (4,4,4)
        #self.input_shape = ?
        self.state_size = len(self.gameState.binary)
        self.action_size = len(self.actionSpace)

    def reset(self):
        self.gameState = GameState(np.zeros(4,4,4))
        self.currentPlayer = 1
        return self.gameState

    def step(self, action):
        next_state, value, done = self.gameState.takeAction(action)
        self.gameState = next_state
        self.currentPlayer = -self.currentPlayer
        info = None
        return (next_state,value,done,info)

    def identities(self, state, actionValues):
        identities = [(state, actionValues)]

        currentBoard = state.board
        currentAV = actionValues

        currentBoard = np.array([currentBoard[0,0,0], currentBoard[0,0,1], currentBoard[0,0,2], currentBoard[0,0,3],
                                 currentBoard[0,1,0], currentBoard[0,1,1], currentBoard[0,1,2], currentBoard[0,1,3],
                                 currentBoard[0,2,0], currentBoard[0,2,1], currentBoard[0,2,2], currentBoard[0,2,3],
                                 currentBoard[0,3,0], currentBoard[0,3,1], currentBoard[0,3,2], currentBoard[0,3,3],

                                 currentBoard[1,0,0], currentBoard[1,0,1], currentBoard[1,0,2], currentBoard[1,0,3],
                                 currentBoard[1,1,0], currentBoard[1,1,1], currentBoard[1,1,2], currentBoard[1,1,3],
                                 currentBoard[1,2,0], currentBoard[1,2,1], currentBoard[1,2,2], currentBoard[1,2,3],
                                 currentBoard[1,3,0], currentBoard[1,3,1], currentBoard[1,3,2], currentBoard[1,3,3],

                                 currentBoard[2,0,0], currentBoard[2,0,1], currentBoard[2,0,2], currentBoard[2,0,3],
                                 currentBoard[2,1,0], currentBoard[2,1,1], currentBoard[2,1,2], currentBoard[2,1,3],
                                 currentBoard[2,2,0], currentBoard[2,2,1], currentBoard[2,2,2], currentBoard[2,2,3],
                                 currentBoard[2,3,0], currentBoard[2,3,1], currentBoard[2,3,2], currentBoard[2,3,3],

                                 currentBoard[3,0,0], currentBoard[3,0,1], currentBoard[3,0,2], currentBoard[3,0,3],
                                 currentBoard[3,1,0], currentBoard[3,1,1], currentBoard[3,1,2], currentBoard[3,1,3],
                                 currentBoard[3,2,0], currentBoard[3,2,1], currentBoard[3,2,2], currentBoard[3,2,3],
                                 currentBoard[3,3,0], currentBoard[3,3,1], currentBoard[3,3,2], currentBoard[3,3,3]])

        currentAV = np.array([currentBoard[0,0,0], currentBoard[0,0,1], currentBoard[0,0,2], currentBoard[0,0,3],
                                 currentBoard[0,1,0], currentBoard[0,1,1], currentBoard[0,1,2], currentBoard[0,1,3],
                                 currentBoard[0,2,0], currentBoard[0,2,1], currentBoard[0,2,2], currentBoard[0,2,3],
                                 currentBoard[0,3,0], currentBoard[0,3,1], currentBoard[0,3,2], currentBoard[0,3,3],

                                 currentBoard[1,0,0], currentBoard[1,0,1], currentBoard[1,0,2], currentBoard[1,0,3],
                                 currentBoard[1,1,0], currentBoard[1,1,1], currentBoard[1,1,2], currentBoard[1,1,3],
                                 currentBoard[1,2,0], currentBoard[1,2,1], currentBoard[1,2,2], currentBoard[1,2,3],
                                 currentBoard[1,3,0], currentBoard[1,3,1], currentBoard[1,3,2], currentBoard[1,3,3],

                                 currentBoard[2,0,0], currentBoard[2,0,1], currentBoard[2,0,2], currentBoard[2,0,3],
                                 currentBoard[2,1,0], currentBoard[2,1,1], currentBoard[2,1,2], currentBoard[2,1,3],
                                 currentBoard[2,2,0], currentBoard[2,2,1], currentBoard[2,2,2], currentBoard[2,2,3],
                                 currentBoard[2,3,0], currentBoard[2,3,1], currentBoard[2,3,2], currentBoard[2,3,3],

                                 currentBoard[3,0,0], currentBoard[3,0,1], currentBoard[3,0,2], currentBoard[3,0,3],
                                 currentBoard[3,1,0], currentBoard[3,1,1], currentBoard[3,1,2], currentBoard[3,1,3],
                                 currentBoard[3,2,0], currentBoard[3,2,1], currentBoard[3,2,2], currentBoard[3,2,3],
                                 currentBoard[3,3,0], currentBoard[3,3,1], currentBoard[3,3,2], currentBoard[3,3,3]])
        identities.append((GameState(currentBoard, state.playerTurn), currentAV))
        return identities

class GameState():
    def __init__(self, board, playerTurn):
        self.board = board
        self.pieces = {'1':'X', '0': '-', '-1':'0'}
    #    self.winners =

