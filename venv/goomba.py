import pygame
from pygame.sprite import Sprite
import math


class Goomba(Sprite):
    def __init__(self, screen, settings):
        super(Goomba, self).__init__()

        self.screen = screen
        self.settings = settings

        self.movementLeft = True
        self.movementRight = False

        self.collideRight = False
        self.collideLeft = False
        self.collideBottom = False
        self.collideTop = False

        self.image = [pygame.image.load("images/enemies/goomba left.png"), pygame.image.load("images/enemies/goomba right.png")]
        for i in range(len(self.image)):
            self.image[i] = pygame.transform.scale(self.image[i], (32, 42))

        self.rect = self.image[0].get_rect()
        self.x = float(self.rect.x)

    def update(self):
        if self.movementLeft == True and self.collideLeft == False: # If left arrow key is pressed and not touching block to the left
            self.x -= .1
        if self.movementRight == True and self.collideRight == False:# If right arrow key is pressed and not touching block to the right
            self.x += 1
        self.rect.x = self.x


    def drawGoomba(self):
        if self.movementLeft:
            self.screen.blit(self.image[0], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)
