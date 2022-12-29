"""
In Alien Invasion, the player controls a rocket ship that appears
at the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.

required objects:
 - screen
 - Rocket ship
 - fleet of aliens

Modules:
- move Rocket ship(left/right)
- shoots 
- increase speed
- run game

Rules :
- If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet
- If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. 
- If the player loses three ships, the game ends.
"""

import sys
import pygame
from setting import Settings
from ship import Ship

class Alien_invasion:
    def __init__(self):
        """ iniatise the game """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_with,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #set background color

        self.ship = Ship(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    print('game has finished')
    def _update_screen(self):
        # redraw the screeen during pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()