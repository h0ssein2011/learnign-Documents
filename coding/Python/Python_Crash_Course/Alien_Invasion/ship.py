import pygame

class Ship:

    #A class to manage ship

    def __init__(self,ai_game):
        # Initilaise the ship and set the starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the image and get the rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        # Draw the ship at the current location
        self.screen.blit(self.image, self.rect)
        



