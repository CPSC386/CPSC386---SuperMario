import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from buildMap import BuildMap
import gameFunctions as gf


def runGame():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption("Super Mario Bros.")
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))

    map = BuildMap(screen, settings)

    floors = Group()
    bricks = Group()
    questionBlocks = Group()
    mushroomBlocks = Group()

    map.makeMap(floors, bricks, questionBlocks, mushroomBlocks)

    pygame.mixer.init()

    while True:
        gf.checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks)
        screen.fill((0, 0, 0))
        map.drawMap(floors, bricks, questionBlocks, mushroomBlocks)

        pygame.display.flip()


runGame()
