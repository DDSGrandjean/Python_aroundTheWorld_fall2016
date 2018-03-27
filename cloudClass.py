"""
    cloudClass.py
    November 21st, 2016

    Class which contains all the clouds
    for AroundTheWorld.py

    Dylan Grandjean
"""
import pygame, random

class CloudClass(pygame.sprite.Sprite):
    def __init__(self, speed):
        """ Initialize the cloudClass and sets up random
            variables which will give each cloud unique
            characteristics in order to give the sky a
            realistic look."""
        pygame.sprite.Sprite.__init__(self)

        #load and prepare the image
        self.image = pygame.image.load("assets/images/clouds/cloudLevel1.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (random.randint(100, 200), random.randint(50, 150)))
        self.rect = self.image.get_rect()

        #create rectangle
        self.rect.centerx = random.randrange(0, 960)
        self.rect.centery = random.randrange(0, 300)
        self.dx = random.randint((speed - 6), (speed - 3))

    def update(self, screen, speed):
        """ Moves the clouds towards the left at a constant
            speed and resets their course once the edge of
            the screen is reached."""
        self.rect.centerx -= self.dx
        if self.rect.right <= 0:
            self.reset(screen, speed)

    def reset(self, screen, speed):
        """ Resets the characteristics of the cloud to give
            it a new look and delays its appearance to give
            the impression of an ever changing sky."""
        #begin countdown
        self.i = random.randint(0, 60)
        self.sec = 0
        self.sec += 1

        #resets cloud
        if self.sec == self.i:
            self.image = pygame.transform.scale(self.image, (random.randint(50, 150), random.randint(50, 150)))
            self.rect = self.image.get_rect()
            self.rect.left = screen.get_width()
            self.rect.centery = random.randrange(0, 300)
            self.dx = random.randint((speed - 6), (speed - 3))
                           
