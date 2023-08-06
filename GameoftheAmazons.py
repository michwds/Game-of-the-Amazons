from enum import Enum, auto
import numpy as np

class Piece(Enum):
    empty = auto()
    arrow = auto()
    whiteQueen = auto()
    blackQueen = auto()

class GameState: 

    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h
        self.game = [[Piece.empty for x in range(w)] for y in range(h)]
        self.counter =  Turn()

    def newGame(self):

        for i in self.width:
            for j in self.height:
                self.game[i][j] = 0
        self.game[0][3] = self.game[0][3] = self.game[6][0] = self.game[9][3] = Piece.blackQueen
        self.game[0][6] = self.game[3][9] = self.game[6][9] = self.game[9][6] = Piece.whiteQueen


    def move(self, xi, yi, xf, yf):
        
        # TODO: so very much

        if self.counter.playerTurn() == 'White':
            if self.game[xi][yi] == Piece.whiteQueen and self.game[xf][yf] == Piece.empty:
                return True
        else:
            return False

    def generateMoveValidationSet(self, x, y):

        def isEmpty(input):
            if input == Piece.empty:
                return True
            else: return False

        valid = []

        for i in range(x, 9):                       # horizontal range check
            if isEmpty(self.game[i][y]) == True:
                valid.append([i, y])
            else: break
        for i in range(x, 0, -1):
            if isEmpty(self.game[i][y]) == True:
                valid.append([i, y])
            else: break

        for i in range(y, 9):                       # vertical range check
            if isEmpty(self.game[x][i]) == True:
                valid.append([x, i])
            else: break
        for i in range(y, 0, -1):
            if isEmpty(self.game[x][i]) == True:
                valid.append([x, i])
            else: break

        # diagonal range validation. squares are [x+i,y+i][x+i,y-i][x-i,y+i][x-i,y-i]. TODO: fix loop syntax
        for i, j in range(x, 9), range(y, 9):       # x+i,y+i
            if isEmpty(self.game[i][j]) == True:
                valid.append([i, j])
            else: break
        for i, j in range(x, 9), range(y, 0, -1):       # x+i,y-i
            if isEmpty(self.game[i][j]) == True:
                valid.append([i, j])
            else: break
        for i, j in range(x, 0, -1), range(y, 9):       # x-i,y+i
            if isEmpty(self.game[i][j]) == True:
                valid.append([i, j])
            else: break
        for i, j in range(x, 0, -1), range(y, 0, -1):       # x-i,y-i
            if isEmpty(self.game[i][j]) == True:
                valid.append([i, j])
            else: break
        return valid

class Turn:

    def __init__(self) -> None:
        self.turnNum = 0
    def next(self):
        self.turnNum+=1
    def playerTurn(self):
        if self.turnNum%2 == 0:
            return 'White'
        else: return 'Black'
    def reset(self):
        self.turnNum=0
