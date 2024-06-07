from enum import Enum, auto

# this is the game engine for my implementation of Game of the Amazons. At some point I'm going to add AI support.

class Piece(Enum):
    empty = auto()
    arrow = auto()
    whiteQueen = auto()
    blackQueen = auto()


class GameState: 

    def __init__(self, size) -> None:
        self.width = self.height = size
        self.game = [[Piece.empty for x in range(self.width)] for y in range(self.height)]
        self.counter = Turn()
        self.phase = Phase()

    def newGame(self):

        for i in self.width:
            for j in self.height:
                self.game[i][j] = 0
        self.game[0][3] = self.game[3][0] = self.game[6][0] = self.game[9][3] = Piece.blackQueen
        self.game[0][6] = self.game[3][9] = self.game[6][9] = self.game[9][6] = Piece.whiteQueen
        self.queens = {(0,3): Queen(0,3, 'Black'), (3,0): Queen(3,0, 'Black'), (6,0): Queen(6,0, 'Black'), (9,3): Queen(9,3, 'Black'),  # dictionary of queens using their position as key
                       (0,6): Queen(0,6, 'White'), (3,9): Queen(3,9, 'White'), (6,9): Queen(6,9, 'White'), (9,6): Queen(9,6, 'White')}
        self.counter.reset()
        self.phase.reset()

    def isOver(self):
        black, white = 0
        for queen in self.queens.values():
            queen.validate()
            match queen.colour:
                case 'Black':
                    if queen.dead == True:
                        black +=1
                case 'White':
                    if queen.dead == True:
                        white +=1
        if black == 4:
            return 'White'
        elif white == 4:
            return 'Black'
        else: return False


    def move(self, initial, final):     # move a piece from initial to final. Must take a pair of tuples as input.
        xi, yi = initial
        xf, yf = final
        queen = self.queens[initial]    
        if final not in queen.moves or queen.dead == True:
            return False
        else:
            self.game[xi][yi] = Piece.empty
            self.game[xf][yf] = queen.colour
            self.queens.pop(initial)
            queen.update(final)
            self.queens[final] = queen
            self.phase.next()
            return True

        
    def shoot(self, target):     # place an arrow at 'target' and advance the phase AND turn. Input must be a tuple.
        x, y = target
        if self.game[x][y] == Piece.empty:
            self.game[x][y] = Piece.arrow
            self.phase.next()
            self.counter.next()
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

class Turn:                     # turn number tracker

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

class Phase:                    # phase tracker
    
    def __init__(self) -> None:
        self.phase = 'Move'
    def next(self):
        if self.phase == 'Move':
            self.phase = 'Shoot'
        else: self.phase = 'Move'
    def current(self):
        return self.phase
    def reset(self):
        self.phase = 'Move'

class Queen:                    # TODO: add a method to count dead queens and end the game when only one queen remains. make sure gamestate.getvalid works
    
    def __init__(self, x, y, colour) -> None:
        self.x = x
        self.y = y
        self.moves = GameState.getValidMoveset(self)
        self.dead = False
        self.colour = colour
    def validate(self):
        self.moves = GameState.getValidMoveset(self)
        if not self.moves:
            self.dead = True
    def update(self, new):
        self.x, self.y = new
        self.validate()

    
    

