class GameStats:
    """Track stats for Mario"""

    def __init__(self):
        self.reset_stats()

        # Declare attributes in init
        self.lives = 3
        self.score = 0
        self.high_score = 0
        self.world = "1-1"
        self.coins = 0

        # Game states
        self.game_active = False
        self.show_hs = False

    def reset_stats(self):
        self.lives = 3
        self.score = 0
        self.world = "1-1"
        self.coins = 0
