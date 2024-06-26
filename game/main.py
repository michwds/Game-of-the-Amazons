from game import engine
from engine import Piece
import pygame as pg

WIDTH = HEIGHT = 600
GAME_SIZE = 10
TILE_SIZE = WIDTH / GAME_SIZE
ASSETS = {}

def loadAssets():
    assetNames = 'whiteQueen', 'blackQueen', 'arrow', 'highlight'
    for a in assetNames:
        ASSETS[a] = pg.image.load('../assets/' + a + '.png')

def main():
    pg.init()
    screen = pg.displayset_mode((WIDTH, HEIGHT))
    gameTime = pg.time.Clock
    game = engine.GameState(GAME_SIZE)
    loadAssets()
    running = True
    selected = ()
    target = ()
    
    while running:                      # main game loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                x = x // TILE_SIZE
                y = y // TILE_SIZE
                if (game.counter.playerTurn() == 'White' and game.game[x][y] == Piece.whiteQueen or
                    game.counter.playerTurn() == 'Black' and game.game[x][y] == Piece.blackQueen):

                    valid = game.queens[(x,y)].moves            #gets the valid moveset for the selected piece
                    if not selected:
                        selected = (x,y)
                        for tile in valid:
                            x, y = tile
                            screen.blit(ASSETS['highlight'], pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)) #TODO: add a highlight to the valid shots, update and remove move highlight after move is completed
                    else:
                        target = (x,y)
                        if target in valid:
                            match game.phase.current():
                                case 'Move':
                                    if game.move(selected, target):  # move the piece
                                        selected = target
                                case 'Shoot':
                                    if game.shoot(target):  # shoot the arrow
                                        selected = ()
                        else:
                            selected = ()

        drawBoard(screen, game)
        gameTime.tick(10)
        pg.display.flip()

def drawBoard(screen, gamestate):       # draws the entire board from the stored gamestate
    for x in range(GAME_SIZE):
        for y in range(GAME_SIZE):
            if ((x+y)%2==0):
                colour = pg.color("white")
            else:
                colour = pg.color("beige")
            pg.draw.rect(screen, colour, pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

            content = gamestate.game[x][y]
            match content:
                case Piece.arrow:
                    pname = 'arrow'
                case Piece.whiteQueen:
                    pname = 'whiteQueen'
                case Piece.blackQueen:
                    pname = 'blackQueen'

            screen.blit(ASSETS[pname], pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))



if __name__ == '__main__':
    main()