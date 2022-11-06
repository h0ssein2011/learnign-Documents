import sys
import pygame

class Alien_invasion:
    def __init__(self):
        """ iniatise the game """
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    print('game has finished')

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()