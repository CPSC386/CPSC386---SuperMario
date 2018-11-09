class GameStats:
    """Track stats for Mario"""

    def __init__(self):
        self.reset_stats()

        # Declare attributes in init
        self.lives = 0
        self.score = 0
        self.high_score = 0

        # Game states
        self.game_active = False

    def reset_stats(self):
        self.lives = 3
        self.score = 0
