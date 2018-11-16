import pygame


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # super mario bros title block
        self.title_image = pygame.image.load('images/mario title.png')
        self.title_image = pygame.transform.scale(self.title_image, (550, 300))
        self.rect = self.title_image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 350

        # Dimensions and properties of buttons
        self.width, self.height = 200, 50
        self.button_color = (100, 100, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # play and high score buttons
        self.hs_image = None
        self.hs_image_rect = None
        self.play_image = None
        self.play_image_rect = None
        self.back_image = None
        self.back_image_rect = None
        self.prep_hs()
        self.prep_play()
        self.prep_back()

    def prep_hs(self):
        self.font = pygame.font.SysFont(None, 48)
        hs = "HIGH SCORE"
        self.hs_image = self.font.render(hs, True, self.text_color, self.button_color)
        self.hs_image_rect = self.hs_image.get_rect()
        self.hs_image_rect.center = self.rect.center
        self.hs_image_rect.top = self.screen_rect.bottom - 125

    def prep_play(self):
        self.font = pygame.font.SysFont(None, 48)
        play = "PLAY GAME"
        self.play_image = self.font.render(play, True, self.text_color, self.button_color)
        self.play_image_rect = self.play_image.get_rect()
        self.play_image_rect.center = self.rect.center
        self.play_image_rect.top = self.screen_rect.bottom - 175

    def prep_back(self):
        self.font = pygame.font.SysFont(None, 48)
        back = "BACK"
        self.back_image = self.font.render(back, True, self.text_color, self.button_color)
        self.back_image_rect = self.back_image.get_rect()
        self.back_image_rect.left = self.screen_rect.left
        self.back_image_rect.bottom = self.screen_rect.bottom

    def blit(self):
        self.screen.fill((100, 100, 200))
        self.screen.blit(self.title_image, self.rect)
        self.screen.blit(self.hs_image, self.hs_image_rect)
        self.screen.blit(self.play_image, self.play_image_rect)

    def blit_back(self):
        self.screen.fill((100, 100, 200))
        self.screen.blit(self.back_image, self.back_image_rect)
