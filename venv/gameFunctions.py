import pygame
import sys


def checkEvents(map, floors, bricks, questionBlocks, mushroomBlocks, settings, stats, start):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks, settings)
        elif event.type == pygame.KEYUP:
            checkUp(event, settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(stats, start, mouse_x, mouse_y)


def checkDown(event, map, floors, bricks, questionBlocks, mushroomBlocks, settings):
    if event.key == pygame.K_RIGHT:
        settings.moving_right = True


def checkUp(event, settings):
    if event.key == pygame.K_RIGHT:
        settings.moving_right = False


def check_buttons(stats, start, mouse_x, mouse_y):
    """Start a new game when player clicks Play"""
    if start.play_image_rect.collidepoint(mouse_x, mouse_y):
        pygame.mouse.set_visible(False)
        stats.game_active = True
        pygame.mixer.music.load('sounds/smb_theme.mp3')
        pygame.mixer.music.play(0)
    # if start.hs_image_rect.collidepoint(mouse_x, mouse_y):

def updateEnemies(goombas, koopas, pipes, invisG):
    if pygame.time.get_ticks() % 4 == 0:
        goombas.update(pipes, invisG)
    if pygame.time.get_ticks() & 4 == 0:
        koopas.update(pipes, invisG)

