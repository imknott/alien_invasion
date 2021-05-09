import json

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize Statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        #Start game in inactive state.
        self.game_active = False
        #High score should never reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def get_stored_highscore(self):
        """Get highscore saved in the highscores.json file."""
        filename = 'highScores.json'
        try:
            with open(filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            return None
        else:
            return self.high_score