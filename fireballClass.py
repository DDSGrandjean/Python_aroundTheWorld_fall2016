"""
    fireballClass.py
    December 5th, 2016

    Class which creates an instance of a
    projectile which is used to kill monsters
    in the game.

    Dylan Grandjean
"""
import pygame
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()
    
class FireballClass(pygame.sprite.Sprite):
    def __init__(self, player, speed):
        """ Initialize the class and pass the player's coordinate and
            current speed of the game."""
        pygame.sprite.Sprite.__init__(self)

        #load image
        self.image = pygame.image.load("assets/images/misc/fireball.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        #create rectangle
        self.rect.left = player.rect.right
        self.rect.centery = player.rect.centery
        self.dx = speed + 12

        #load sound
        self.fireSound = pygame.mixer.Sound("assets/sounds/friendlyFire.ogg")

    def update(self, grounded):
        """ Shoots a fireball from the players position."""
        self.rect.centerx += self.dx

    def playSound(self):
        """ Play sound when player fires."""
        self.fireSound.play()
