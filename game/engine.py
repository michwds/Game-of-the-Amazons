from enum import Enum, auto


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

    def getValidMoveset(self, queen):

        def isEmpty(input):                         # check if target tile is empty
            if input == Piece.empty:
                return True
            else: return False

        x = queen.x
        y = queen.y
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
                                                    # diagonal range checks
        for i in range(0, 9):       # x+i,y+i
            if isEmpty(self.game[x+i][y+i]) == True:
                valid.append([x+i, y+i])
            else: break
        for i in range(0, 9):       # x+i,y-i
            if isEmpty(self.game[x+i][y-i]) == True:
                valid.append([x+i, y-i])
            else: break
        for i in range(0, 9):       # x-i,y+i
            if isEmpty(self.game[x-i][y+i]) == True:
                valid.append([x-i, y+i])
            else: break
        for i in range(0, 9):       # x-i,y-i
            if isEmpty(self.game[x-i][y-i]) == True:
                valid.append([x-i, y-i])
            else: break
        if valid:                                   #update list of valid moves. If none, mark the queen as dead
            queen.moves = valid
        else:
            queen.moves = valid
            queen.dead = True

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

class Queen:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.moves = GameState.getValidMoveset(self.x, self.y)
        self.dead = False
    

