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
            self.image[i] = pygame.transform.scale(self.image[i], (32, 48))

        self.rect = self.image[0].get_rect()

    def update(self, pipes, invisG):
        self.checkCollision(pipes, invisG)
        x = self.rect.x
        if self.movementLeft and self.collideLeft == False:
            x -= 1
        if self.movementRight and self.collideRight == False:
            x += 1
        self.rect.x = x


    def drawGoomba(self):
        if self.movementLeft:
            self.screen.blit(self.image[0], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)

    def checkCollision(self, pipes, invisG):
        for pipe in pipes:
            if pygame.sprite.collide_rect(self, pipe):
                if self.movementLeft:
                    self.rect.x += 2
                    self.movementLeft = False
                    self.collideLeft = self.movementRight = True
                elif self.movementRight:
                    self.rect.x -= 2
                    self.movementRight = False
                    self.collideRight = self.movementLeft = True
            else:
                self.collideLeft = self.collideRight = False
        for invis in invisG:
            if pygame.sprite.collide_rect(self, invis):
                if self.movementLeft:
                    self.rect.x += 2
                    self.movementLeft = False
                    self.collideLeft = self.movementRight = True
                elif self.movementRight:
                    self.rect.x -= 2
                    self.movementRight = False
                    self.collideRight = self.movementLeft = True
            else:
                self.collideLeft = self.collideRight = False
