"""
    backgroundClass.py
    December 9th, 2016

    Class which creates scrolling background
    images to give life to the environment.
    
    Dylan Grandjean
"""
import pygame

class BackgroundClass(pygame.sprite.Sprite):
    def __init__(self, image, speed, diff):
        """ Initialize the class.
            Get images, speed, and diff
            from the main method in order to
            create a more polyvalent class."""
        pygame.sprite.Sprite.__init__(self)
        
        #load sprite
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))

        #create rectangle for that sprite
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

        #set up variables
        self.diff = diff
        self.dx = speed + self.diff

    def update(self, screen, speed):
        """ Moves the backgroun towards
            the left with every frame
            at a given speed minus a
            constant difference."""
        self.rect.centerx -= self.dx
        if self.rect.right < screen.get_width():
            self.reset(speed, self.diff)

    def reset(self, speed, diff):
        """ Resets the background when the
            right side of the image reaches
            the edge of the screen."""
        self.rect.left = 0
        self.dx = speed + self.diff
        
