"""
    electrostatics.py
    December 8th, 2016

    Simple electrostatic shockwaves which are
    added to the game for effect.

    Dylan Grandjean
"""
import pygame

class Electrostatics(pygame.sprite.Sprite):
    def __init__(self):
        """ Initialize the class"""
        pygame.sprite.Sprite.__init__(self)

        #load image
        self.image = pygame.image.load("assets/images/grounds/electrostatics.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))

        #create a rectangle
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = 512

        #create a speed
        self.dx = 40\

    def update(self, screen):
        """ Resets the shockwave's position whenever
            it exists the screen."""
        self.rect.centerx += self.dx
        if self.rect.left > screen.get_width():
            self.rect.right = 0
        
        
