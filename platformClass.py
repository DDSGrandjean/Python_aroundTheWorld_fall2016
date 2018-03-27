"""
    platformClass.py
    November 21st, 2016

    Class which creates platforms
    randomly of various sizes.

    Dylan Grandjean
"""
import pygame, random

class PlatformClass(pygame.sprite.Sprite):
    def __init__(self, row, speed):
        """ Initialize class and pass in a row value and the current
            game speed."""
        pygame.sprite.Sprite.__init__(self)

        #assign a row value to the platform. This value won't ever change
        self.row = row

        #assign random values for reseting purposes
        self.i = random.randint(30,240)
        self.x = random.randint(960, 3000)
        self.sec = 0

        #load images
        self.images = []
        self.images.append(pygame.image.load("assets/images/platforms/platform[0].png"))
        self.images.append(pygame.image.load("assets/images/platforms/platform[1].png"))
        self.images.append(pygame.image.load("assets/images/platforms/platform[2].png"))

        #determine platform size and create rectangle
        self.n = random.randint(0, 2)
        self.image = self.images[self.n]
        self.image = self.image.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        #determine coordinates
        self.rect.left = self.x
        self.rect.centery = self.row

        #initialize speed relative to game speed
        self.dx = speed

    def update(self, screen, speed):
        """ Move the platform towards the left and resets its position
            and size whenever it exists the screen."""
        self.rect.centerx -= speed
        if self.rect.right < 0:
            self.sec += 1
            if self.sec == self.i:
                self.reset(screen)

    def reset(self, screen):
        """ Changes the size, rectangle, and image of platform
            whenever it exists the screen."""
        #assign new random values for resetting purposes
        self.i = random.randint(30,240)
        self.sec = 0

        #detemrine new size, image and rectangle
        self.n = random.randint(0, 2)
        self.image = self.images[self.n]
        self.image = self.image.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        #determine nes coordinates
        self.rect.left = screen.get_width()
        self.rect.centery = self.row
        
        
