"""
    skiesClass.py
    November 21st, 2016

    Class which loads a simple sky background

    Dylan Grandjean
"""
import pygame

class SkiesClass(pygame.sprite.Sprite):
    def __init__(self):
        """ Initialize class."""
        pygame.sprite.Sprite.__init__(self)

        #load image
        self.image = pygame.image.load("assets/images/skies/skyLevel1.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
                           
