import pygame
from pygame.sprite import Sprite


class Block(Sprite):  # item will default to -1 and quantity will default to 0 if nothing is passed when init
    def __init__(self, screen, settings, skin, item=-1, quantity=0):
        super(Block, self).__init__()
        self.screen, self.settings = screen, settings
        self.skin = skin
        self.item = item
        self.quantity = quantity
        
        if skin == 0:
            self.image = pygame.image.load("images/1-1/unbreakable brick.png")
        elif skin == 1:
            self.image = pygame.image.load("images/1-2/unbreakable brick.png")
        elif skin == 2:
            self.image = pygame.image.load("images/1-1/now empty brick.png")
        elif skin == 3:
            self.image = pygame.image.load("images/1-2/now empty brick.png")
        elif skin == 4:
            self.image = pygame.image.load("images/1-1/breakable brick.png")
        elif skin == 5:
            self.image = pygame.image.load("images/1-2/breakable brick.png")
        elif skin == 6:
            self.image = pygame.image.load("images/1-1/surprise brick.png")
        elif skin == 7:
            self.image = pygame.image.load("images/1-2/surprise brick.png")
        elif skin == 8:
            self.image = pygame.image.load("images/1-1/sky.png")
            # self.image = self.image.convert_alpha()
            # self.image.set_alpha(0)

        self.image = pygame.transform.scale(self.image, (settings.rectSize, settings.rectSize))
        self.rect = self.image.get_rect()

        if self.skin >= 4:
            self.hitRect = pygame.Rect(0, 0, settings.rectSize, settings.rectSize/6)
            self.hitRect.x, self.hitRect.y = self.rect.x, self.rect.bottom + 20

    def update(self):
        if self.item == 0:
            print("item 0 should pop out")
            self.quantity -= 1
            if self.quantity <= 0:
                self.skin = 2
                self.image = pygame.image.load("images/1-1/now empty brick.png")

    def blit(self):
        self.screen.blit(self.image, self.rect)

        if self.skin >= 4:  # this is here for future Collisions to ge items to pop out
            self.hitRect.x, self.hitRect.y = self.rect.x, self.rect.bottom
            pygame.draw.rect(self.screen, (0, 0, 0), self.hitRect)
