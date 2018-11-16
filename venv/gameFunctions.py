import pygame
import sys


def check_events(settings, stats, start):
    # def check_events(map, floors, bricks, question_blocks, mushroom_blocks, settings, stats, start):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # check_down(event, map, floors, bricks, question_blocks, mushroom_blocks, settings)
            check_down(event, settings)
        elif event.type == pygame.KEYUP:
            check_up(event, settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(stats, start, mouse_x, mouse_y)


# def check_down(event, map, floors, bricks, question_blocks, mushroom_blocks, settings):
def check_down(event, settings):
    if event.key == pygame.K_RIGHT:
        settings.moving_right = True


def check_up(event, settings):
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


def update_enemies(goombas, koopas, pipes, invis_g):
    if pygame.time.get_ticks() % 4 == 0:
        goombas.update(pipes, invis_g)
    if pygame.time.get_ticks() & 4 == 0:
        koopas.update(pipes, invis_g)
