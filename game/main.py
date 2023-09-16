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
    game = engine.GameState()
    loadAssets()
    running = True
    
    while running:                      # main game loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
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