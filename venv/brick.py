import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, screen, settings):
        super(Brick, self).__init__()
        self.screen, self.settings = screen, settings
        self.image = pygame.image.load("images/1-1/breakable brick.png")
        self.image = pygame.transform.scale(self.image, (settings.rectSize, settings.rectSize))
        self.rect = self.image.get_rect()

    def blit(self):
        self.screen.blit(self.image, self.rect)