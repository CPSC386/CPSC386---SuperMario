import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from buildMap import BuildMap
from game_stats import GameStats
from start_screen import StartScreen
from mario import Mario
from block import Block # TESTING DIVERSE BLOCK
import gameFunctions as gf


def runGame():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption("Super Mario Bros.")
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))

    map = BuildMap(screen, settings)
    stats = GameStats()
    start = StartScreen(screen)
    mario = Mario(screen, settings)

    testBlocks = []
    blocks = Group()
    for i in range(8): # Testing the Diverse Block
        block = Block(screen, settings, i)
        block.rect.x, block.rect.y = 50+(50*i), settings.screenHeight - 100
        testBlocks.append(block)

    floors = Group()
    bricks = Group()
    questionBlocks = Group()
    mushroomBlocks = Group()
    unbreakableBricks = Group()
    pipes = Group()

 #   map.makeMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)
    map.makeMap(floors, blocks, pipes)
    pygame.mixer.init()

    while True:
        if stats.game_active:
            screen.fill((100, 100, 200))
            gf.checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings, stats, start)
#            map.shiftMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes, settings)
            map.shiftMap(floors, blocks, pipes, settings)
#            map.drawMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)
            map.drawMap(floors, blocks, pipes)


            mario.drawPlayer()
            for block in testBlocks: # testing Diverse Block
                block.blit()

            pygame.display.flip()
        else:
            start.blit()
#            map.drawMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)
            map.drawMap(floors, blocks, pipes)

            gf.checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings, stats, start)
            pygame.display.flip()


runGame()
