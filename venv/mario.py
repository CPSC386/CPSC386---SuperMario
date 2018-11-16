import pygame
import math


class Mario:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.movementLeft = False
        self.movementRight = False

        self.collideRight = False
        self.collideLeft = False
        self.collideBottom = False
        self.collideTop = False

        self.image = [pygame.image.load("images/mario/mario/right1.png"),
                      pygame.image.load("images/mario/mario/right2.png"),
                      pygame.image.load("images/mario/mario/right3.png"),
                      pygame.image.load("images/mario/mario/right4.png")]
        for i in range(len(self.image)):
            self.image[i] = pygame.transform.scale(self.image[i], (40, 50))

        self.rect = self.image[0].get_rect()
        self.x, self.y = 100, self.settings.screenHeight - self.rect.bottom - 200
        self.rect.x, self.rect.y = self.x, self.y

    def update_player(self):
        if not self.collideBottom:
            self.y += self.settings.playerSpeed * 2
        if self.movementLeft and not self.collideLeft:  # If left key is pressed and not touching block to the left
            self.x -= self.settings.playerSpeed
        if self.movementRight and not self.collideRight:  # If right key is pressed and not touching block to the right
            self.x += self.settings.playerSpeed

        self.rect.x, self.rect.y = self.x, self.y

    def draw_player(self):
        if pygame.time.get_ticks() % 1200 < 300:
            # self.rect = self.image[0].get_rect()
            self.screen.blit(self.image[0], self.rect)
        elif pygame.time.get_ticks() % 1200 < 600:
            # self.rect = self.image[1].get_rect()
            self.screen.blit(self.image[1], self.rect)
        elif pygame.time.get_ticks() % 1200 < 900:
            # self.rect = self.image[2].get_rect()
            self.screen.blit(self.image[2], self.rect)
        else:
            # self.rect = self.image[3].get_rect()
            self.screen.blit(self.image[3], self.rect)

    def reset(self):
        self.x = 50
        self.y = self.settings.screenHeight - 100
