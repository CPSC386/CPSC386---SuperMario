import pygame
from pygame.sprite import Group


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, settings, screen, stats, start_screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.start = start_screen

        # Font settings
        self.text_color = (255, 255, 255)
        self.bg_color = (100, 100, 200)
        self.font = pygame.font.SysFont(None, 48)

        # Declare attributes in init but initialize in other methods
        self.score_image = None
        self.score_rect = None
        self.value_image = None
        self.value_rect = None
        self.lives_str_image = None
        self.lives_str_rect = None
        self.lives_image = None
        self.lives_rect = None
        self.coins_image = None
        self.coins_rect = None
        self.num_coins_image = None
        self.num_coins_rect = None
        self.world_image = None
        self.world_rect = None
        self.curr_image = None
        self.curr_image_rect = None
        self.hs_image = None
        self.hs_rect = None

        # Prepare the initial score images
        self.prep_score()
        self.prep_lives()
        self.prep_coins()
        self.prep_world()

    def prep_score(self):
        """Turn score into a rendered image"""
        score = "SCORE"
        rounded_score = round(self.stats.score, -1)
        value = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score, True, self.text_color, self.bg_color)
        self.value_image = self.font.render(value, True, self.text_color, self.bg_color)

        # Display score at top left
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = self.screen_rect.top

        self.value_rect = self.value_image.get_rect()
        self.value_rect.left = self.screen_rect.left + 65
        self.value_rect.top = 30

    def prep_lives(self):
        lives_str = "LIVES"
        self.lives_str_image = self.font.render(lives_str, True, self.text_color, self.bg_color)
        lives = str(self.stats.lives)
        self.lives_image = self.font.render(lives, True, self.text_color, self.bg_color)

        # Display at top right
        self.lives_str_rect = self.lives_str_image.get_rect()
        self.lives_str_rect.right = self.screen_rect.right - 20
        self.lives_str_rect.top = self.screen_rect.top

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.right - 65
        self.lives_rect.top = 30

    def prep_coins(self):
        coins = "COINS"
        num_coins = str(self.stats.coins)
        self.coins_image = self.font.render(coins, True, self.text_color, self.bg_color)
        self.num_coins_image = self.font.render(num_coins, True, self.text_color, self.bg_color)

        # Display coins at middle-left
        self.coins_rect = self.coins_image.get_rect()
        self.coins_rect.left = self.screen_rect.left + 350
        self.coins_rect.top = self.screen_rect.top

        self.num_coins_rect = self.value_image.get_rect()
        self.num_coins_rect.left = self.screen_rect.left + 390
        self.num_coins_rect.top = 30

    def prep_world(self):
        world = "WORLD"
        curr_world = self.stats.world
        self.world_image = self.font.render(world, True, self.text_color, self.bg_color)
        self.curr_image = self.font.render(curr_world, True, self.text_color, self.bg_color)

        # Display world at middle-right
        self.world_rect = self.world_image.get_rect()
        self.world_rect.right = self.screen_rect.right - 350
        self.world_rect.top = self.screen_rect.top

        self.curr_image_rect = self.curr_image.get_rect()
        self.curr_image_rect.right = self.screen_rect.right - 390
        self.curr_image_rect.top = 30

    def show_score(self):
        """Draw scoreboard to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.value_image, self.value_rect)
        self.screen.blit(self.lives_str_image, self.lives_str_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
        self.screen.blit(self.coins_image, self.coins_rect)
        self.screen.blit(self.num_coins_image, self.num_coins_rect)
        self.screen.blit(self.world_image, self.world_rect)
        self.screen.blit(self.curr_image, self.curr_image_rect)

    def show_hs(self):
        self.screen.fill((100, 100, 200))
        value = str(self.stats.high_score)
        hs = "HIGH SCORE: " + value
        self.hs_image = self.font.render(hs, True, self.text_color, self.bg_color)

        self.hs_rect = self.hs_image.get_rect()
        self.hs_rect.center = self.screen_rect.center
        self.hs_rect.top = self.screen_rect.top

        self.start.blit_back()
        self.screen.blit(self.hs_image, self.hs_rect)
        pygame.display.flip()
