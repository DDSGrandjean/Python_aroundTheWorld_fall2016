"""
    groundClass.py
    November 21st, 2016

    Class which controls the behavior of the
    ground on which the player can run.

    Dylan Grandjean
"""
import pygame

class GroundClass(pygame.sprite.Sprite):
    def __init__(self, speed):
        """ Initialize the class and pass the speed of the game."""
        pygame.sprite.Sprite.__init__(self)

        #load image
        self.image = pygame.image.load("assets/images/grounds/groundLevel2.png")
        self.image = self.image.convert()

        #create rectangle
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = 512

        #initialize speed
        self.dx = speed

    def update(self, screen, speed):
        """ Moves the ground towards the left at a constant
            speed equal to the game's speed."""
        self.rect.right -= speed
        if self.rect.right < screen.get_width():
            self.reset(screen)

    def reset(self, screen):
        """Resets the ground to its original position whenever
            its right side reaches the edge of the screen."""
        self.rect.left = 0
                           
