import pygame


def checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks)
        elif event.type == pygame.KEYUP:
            checkUp(event)


def checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks):
    if event.key == pygame.K_RIGHT:
        print("right")
        map.shiftMap(floors, bricks, questionBlocks, mushroomBlocks)


def checkUp(event):
    if event.key == pygame.K_RIGHT:
        print(".")
