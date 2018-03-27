"""
    coinsClass.py
    December 12th, 2016

    Creates coins which can be picked up by
    the player in order to get more points
    for this run.
    
    Dylan Grandjean
"""
import pygame, random
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()

class CoinsClass(pygame.sprite.Sprite):
    def __init__(self, speed):
        """ Initialize the class and creates
            characteristics unique to each coin."""
        pygame.sprite.Sprite.__init__(self)

        #load image and create rectanlge
        self.image = pygame.image.load("assets/images/misc/coin.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        #load sound
        self.coinSound = pygame.mixer.Sound("assets/sounds/coinsSound.ogg")

        #realm of y coordinates in which the coin can appear
        self.coord = [32, 160, 288, 416]

        #other variable's random instantiation
        self.rect.centery = random.choice(self.coord)
        self.rect.centerx = random.randint(1000, 3000)

    def update(self, screen, speed):
        """ Moves the coin towards the left at a
            constant speed equal to the speed
            of the game, and resets its position once
            the edge of the screen is reached."""
        self.rect.centerx -= speed
        if self.rect.right < 0:
            self.reset(screen)

    def reset(self, screen):
        """ Gives the coin a new y coordinate and a
            random position x ahead of the player."""
        self.rect.left = screen.get_width()
        self.rect.centery = random.choice(self.coord)
        self.rect.centerx = random.randint(1000, 3000)

    def playSound(self):
        """ Play sound when coin is picked up."""
        self.coinSound.play()
                       
