import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from buildMap import BuildMap
from game_stats import GameStats
from start_screen import StartScreen
from mario import Mario
from block import Block  # TESTING DIVERSE BLOCK
import gameFunctions as Gf


def run_game():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption("Super Mario Bros.")
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))

    map = BuildMap(screen, settings)
    stats = GameStats()
    start = StartScreen(screen)
    mario = Mario(screen, settings)

    test_blocks = []
    blocks = Group()
    for i in range(8):  # Testing the Diverse Block
        block = Block(screen, settings, i)
        block.rect.x, block.rect.y = 50+(50*i), settings.screenHeight - 100
        test_blocks.append(block)

    floors = Group()
    # bricks = Group()
    # question_blocks = Group()
    # mushroom_blocks = Group()
    # unbreakableBricks = Group()
    pipes = Group()
    goombas = Group()
    invis_g = Group()
    koopas = Group()

    # map.makeMap(floors, bricks, question_blocks, mushroom_blocks, unbreakableBricks, pipes)
    map.make_map(floors, blocks, pipes, goombas, invis_g, koopas)
    pygame.mixer.init()

    while True:
        if stats.game_active:
            screen.fill((100, 100, 200))
            # Gf.check_events(map, floors, bricks, question_blocks, mushroom_blocks, settings, stats, start)
            Gf.check_events(settings, stats, start)
#            map.shiftMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes, settings)
            map.shift_map(floors, blocks, pipes, settings, goombas, invis_g, koopas)
#            map.drawMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)
            map.draw_map(floors, blocks, pipes, goombas, invis_g, koopas)
            Gf.update_enemies(goombas, koopas, pipes, invis_g)

            mario.draw_player()
            for block in test_blocks:  # testing Diverse Block
                block.blit()

            pygame.display.flip()
        else:
            start.blit()
#            map.drawMap(floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes)
            map.draw_map(floors, blocks, pipes, goombas, invis_g, koopas)

            # Gf.check_events(map, floors, bricks, question_blocks, mushroom_blocks, settings, stats, start)
            Gf.check_events(settings, stats, start)
            pygame.display.flip()


run_game()
