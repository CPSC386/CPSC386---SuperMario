import pygame
from pygame.sprite import Sprite
import math


class Koopa(Sprite):
    def __init__(self, screen, settings):
        super(Koopa, self).__init__()

        self.screen = screen
        self.settings = settings

        self.movementLeft = True
        self.movementRight = False

        self.collideRight = False
        self.collideLeft = False
        self.collideBottom = False
        self.collideTop = False

        self.image = [pygame.image.load("images/enemies/koopa left1.png"),
                      pygame.image.load("images/enemies/koopa left2.png"),
                      pygame.image.load("images/enemies/koopa right1.png"),
                      pygame.image.load("images/enemies/koopa right2.png")]
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

    def draw_koopa(self):
        if self.movementLeft:
            if pygame.time.get_ticks() % 600 < 300:
                self.screen.blit(self.image[0], self.rect)
            else:
                self.screen.blit(self.image[1], self.rect)

        else:
            if pygame.time.get_ticks() % 600 < 300:
                self.screen.blit(self.image[2], self.rect)
            else:
                self.screen.blit(self.image[3], self.rect)

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
