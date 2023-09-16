from game import engine
import pygame as pg

WIDTH = HEIGHT = 600
GAME_SIZE = 10
TILE_SIZE = WIDTH / GAME_SIZE
ASSETS = {}

def loadAssets():
    assetNames = 'whiteQueen', 'blackQueen', 'arrow', 'lightTile', 'darkTile', 'highlight'
    for a in assetNames:
        ASSETS[a] = pg.image.load('../assets/' + a + '.png')