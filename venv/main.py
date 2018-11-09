import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from buildMap import BuildMap
from game_stats import GameStats
from start_screen import StartScreen
import gameFunctions as gf


def runGame():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption("Super Mario Bros.")
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))

    map = BuildMap(screen, settings)
    stats = GameStats()
    start = StartScreen(screen)

    floors = Group()
    bricks = Group()
    questionBlocks = Group()
    mushroomBlocks = Group()
    unbreakableBricks = Group()
    pipes = Group()

    map.makeMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)

    pygame.mixer.init()

    while True:
        if stats.game_active:
            gf.checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings, stats, start)
            map.shiftMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes, settings)
            screen.fill((0, 0, 0))
            map.drawMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)

            pygame.display.flip()
        else:
            start.blit()
            map.drawMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)
            gf.checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings, stats, start)
            pygame.display.flip()


runGame()
