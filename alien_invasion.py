import sys

import pygame

class AlienInvasion:
    """Main class to manage it all."""
    def __init__(self):
        """Initialize the game, and start the window."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Set background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Capture mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw background every time game runs
            self.screen.fill(self.bg_color)

            # display game window
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    """Create a game instance"""
    ai = AlienInvasion()
    ai.run_game()
