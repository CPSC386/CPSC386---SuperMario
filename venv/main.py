import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from buildMap import BuildMap


def runGame():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Super Mario Bros.")

    map = BuildMap(screen, settings)

    floors = Group()
    bricks = Group()
    questionBlocks = Group()

    map.makeMap(floors, bricks, questionBlocks)

    pygame.mixer.init()

    while True:
        screen.fill((0, 0, 0))
        map.drawMap(floors, bricks, questionBlocks)

        pygame.display.flip()



runGame()