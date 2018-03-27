"""
    livesBoxClass.py
    December 12th, 2016

    Class which creates a box the player can
    pick up to gain additional lives during the
    game's running time.

    Dylan Grandjean
"""
import pygame, random
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()

class LivesBoxClass(pygame.sprite.Sprite):
    def __init__(self):
        """ Initialize the class."""
        pygame.sprite.Sprite.__init__(self)

        #load and prepare image
        self.image = pygame.image.load("assets/images/misc/livesBox.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))

        #create rectangle
        self.rect = self.image.get_rect()

        #load sound
        self.boxSound = pygame.mixer.Sound("assets/sounds/lifeBoxSound.ogg")

        #realm of y-coordinates where the create can appear
        self.coord = [32, 160, 288, 416]

        #create random starting coordinates
        self.rect.centery = random.choice(self.coord)
        self.rect.centerx = random.randint(5000, 10000)

    def update(self, screen, speed):
        """ Moves the box towards the left at game's speed
            and resets its position whenever it is picked up
            or leaves the screen."""
        self.rect.centerx -= speed
        if self.rect.right < 0:
            self.rect.centery = random.choice(self.coord)
            self.rect.centerx = random.randint(5000, 10000)

    def playSound(self):
        """ Play sound when player picks up a box."""
        self.boxSound.play()
            
