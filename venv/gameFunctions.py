import pygame
import sys


def checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks, settings)
        elif event.type == pygame.KEYUP:
            checkUp(event, settings)


def checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks, settings):
    if event.key == pygame.K_RIGHT:
        settings.moving_right = True


def checkUp(event, settings):
    if event.key == pygame.K_RIGHT:
        settings.moving_right = False
