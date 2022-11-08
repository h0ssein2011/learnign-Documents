import sys
import pygame
from setting import Settings

class Alien_invasion:
    def __init__(self):
        """ iniatise the game """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_with,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #set background color
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    print('game has finished')
            # redraw the screeen during pass through the loop
            self.screen.fill(self.settings.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()