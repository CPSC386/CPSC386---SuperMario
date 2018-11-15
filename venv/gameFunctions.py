import pygame
import sys


def checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings, stats, start, mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks, settings, mario)
        elif event.type == pygame.KEYUP:
            checkUp(event, settings, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(stats, start, mouse_x, mouse_y)


def checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks, settings, mario):
    # if event.key == pygame.K_RIGHT:
        # settings.moving_right = True
    if event.key == pygame.K_UP:
        mario.movementUp = True
    if event.key == pygame.K_RIGHT:
        mario.movementRight = True
    if event.key == pygame.K_LEFT:
        mario.movementLeft = True


def checkUp(event, settings, mario):
    # if event.key == pygame.K_RIGHT:
        # settings.moving_right = False
    if event.key == pygame.K_UP:
        mario.movementUp = False
    if event.key == pygame.K_RIGHT:
        mario.movementRight = False
    if event.key == pygame.K_LEFT:
        mario.movementLeft = False


def check_buttons(stats, start, mouse_x, mouse_y):
    """Start a new game when player clicks Play"""
    if start.play_image_rect.collidepoint(mouse_x, mouse_y):
        pygame.mouse.set_visible(False)
        stats.game_active = True
    # if start.hs_image_rect.collidepoint(mouse_x, mouse_y):