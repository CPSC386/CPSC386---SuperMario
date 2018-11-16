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

        self.image = [pygame.image.load("images/enemies/goomba left.png"),
                      pygame.image.load("images/enemies/goomba right.png")]
        for i in range(len(self.image)):
            self.image[i] = pygame.transform.scale(self.image[i], (32, 48))

        self.rect = self.image[0].get_rect()

    def update(self, pipes, invis_g):
        self.check_collision(pipes, invis_g)
        x = self.rect.x
        if self.movementLeft and not self.collideLeft:
            x -= 1
        if self.movementRight and not self.collideRight:
            x += 1
        self.rect.x = x

    def draw_goomba(self):
        if self.movementLeft:
            self.screen.blit(self.image[0], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)

    def check_collision(self, pipes, invis_g):
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
        for invis in invis_g:
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
